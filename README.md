Tools for Program Chairs of peer-reviewed conferences
-----------------------------------------------------

Peer-reviewed conferences (such as machine learning conferences in computer science) are seeing a continued increase in submission numbers. Even a medium-sized conference like ECMLPKDD received a record 1200 abstract submissions in 2022. Such scale brings both a wide range of behaviours (including malicious ones) and does not allow to manually check large parts of the submissions.

This repository hosts scripts to aid program chairs in semi-automatically tracking and verifying that PDFs, conflicts, bids, paper assignments and reviews follow the conference guidelines.

For now, it only contains the PDF analysis script, already very valuable to save chairs on having to send desk reject emails (or handle the reviewers reporting them).

Overview of tools:

   * 01_analyze_pdfs: analyse PDFs for length, margins and emails (anonymity). It is recommended to run this 24 hours before the final submission deadline! Will save you many desk rejects...
   * 02_analyze_conflicts: ... TODO clean and release
   * 03a_analyze_bidding: ... TODO clean and release
   * 03b_clean_bids: ... TODO clean and release
   * 04_assignment_helper: ... TODO clean and release
   * 05_analyze_reviews: ... TODO clean and release

How to contribute
-----------------

We welcome pull requests that extend the functionality, including notebooks and tools compatible with submission systems other then Microsoft's CMT3 system (which was used in ECMLPKDD22, for which these tools were initally developed).

