import os
import random
import math
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    ret = {k: 0 for k in corpus}
    lenCorpus = len(corpus)
    links = corpus[page]
    if not links:
        for k, v in corpus.items():
            ret[k] = 1 / lenCorpus
        return ret
    link_prob = damping_factor / len(links) if len(links) else 0
    random_prob = (1 - damping_factor) / lenCorpus
    for link in links:
        ret[link] += link_prob
    for k, v in corpus.items():
        ret[k] += random_prob
    return ret


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    visits = {page: 0 for page in corpus}
    current_page = random.choice(list(corpus.keys()))
    visits[current_page]+=1

    for i in range(n-1):
        model = transition_model(corpus, current_page, damping_factor)

        rand = random.random()
        cumulative_proba = 0
        for page, proba in model.items():
            cumulative_proba += proba
            if rand <= cumulative_proba:
                current_page = page
                break
        visits[current_page]+=1
    
    return {page: nb_visits/n for page, nb_visits in visits.items()}

EPSILON = .001

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    lenCorpus = len(corpus)
    pageRank = {page: 1 / lenCorpus for page in corpus}
    stop = False
    while not stop:
        oldpageRank = pageRank.copy()
        for page in pageRank:
            surf_prob = 0
            for other in pageRank:
                if not corpus[other]:
                    surf_prob += pageRank[other] * (1/lenCorpus)
                elif page in corpus[other]:
                    surf_prob += pageRank[other] / len(corpus[other])
            pageRank[page] = ((1 - damping_factor) / lenCorpus) + (damping_factor * surf_prob)
        norm_factor = sum(pageRank.values())
        pageRank = {page: (rank / norm_factor) for page, rank in pageRank.items()}
        stop = True
        for page in corpus:
            if abs(pageRank[page] - oldpageRank[page]) > EPSILON:
                stop = False
                break
                
    return pageRank


if __name__ == "__main__":
    main()
