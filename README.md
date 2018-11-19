# Wikidata_PageRank

## Dataset
### Wikidata
- URL: http://downloads.dbpedia.org/3.9/en/page_links_en.ttl.bz2
- Dataset sample: `<http://dbpedia.org/resource/AfghanistanHistory> <http://dbpedia.org/ontology/wikiPageWikiLink> <http://dbpedia.org/resource/History_of_Afghanistan> .`
- Dataset format:

  | column | description |
  | :-: | :-:|
  | 0 | link from |
  | 1 | we don't need to care about |
  | 2 | link to |
 
 ### California Data
 - URL: http://www.cs.cornell.edu/courses/cs685/2002fa/data/gr0.California
 - Dataset sample:
    - `n 0 http://www.berkeley.edu/` (the page index of http://www.berkeley.edu/ is 0)
    - `e 80 3301` ( there is a link from page 80 to page 3301)
