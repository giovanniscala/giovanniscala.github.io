---
# An instance of the Pages widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: featured
active: true

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 50

title: Featured Publications
subtitle: ''

content:
  # Page type to display. E.g. post, talk, publication...
  page_type: publication
  # Choose how much pages you would like to display (0 = all pages)
  count: 3
  # Choose how many pages you would like to offset by
  offset: 0
  # Page order: descending (desc) or ascending (asc) date.
  order: desc
  # Filter on criteria
  filters:
    tag: ''
    category: ''
    publication_type: ''
    author: ''
    exclude_featured: false
    featured_only: true
design:
  # Choose a view for the listings:
  #   1 = List
  #   2 = Compact
  #   3 = Card
  #   4 = Citation (publication only)
  columns: "1"
  view: 3
  spacing:
    padding: ["20px", "0", "20px", "0"]
# cta:
#  label: "See All Publications"
#  url: "publications/"
#  icon_pack: "fas"
#  icon: "arrow-right"
---
<!--
 <div class="text-center">
  <a href="/publication/" class="btn btn-outline-primary">
    <i class="fas fa-arrow-right"></i> See all publications
  </a>
</div>
-->
{{% callout note %}}
See all publications [here](./publication/).
{{% /callout %}}
