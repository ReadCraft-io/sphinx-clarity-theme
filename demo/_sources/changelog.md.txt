# Changelog

All notable changes to the project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- 
% ## [x.y.z] - MMMM-MM-DD
%
% - added:
% - fixed:
% - changed:
% - removed:
-->

## [1.2.0] - 2026-03-07

- added: version select - dropdown UI, configuration, client-side redirection
- added: enhance article footer with edit and view page source
- added: type hints for `html_theme_options` for better DX

## [1.1.0] - 2026-02-27

- added: header title: show by default, option to hide it and set it to custom value

## [1.0.3] - 2026-02-26

- fixed: sidebar overflows over horizontal rule
- added: add basic styles for API signatures
- fixed: header menu isn't of the same color as builtin buttons, if displayed "as": "button"
- fixed: header menu on mobile is shown even when empty
- fixed: missing header padding on tablet
- fixed: next/prev are not on right/left on first/last page
- fixed: missing "." in footer between author and "Made with..."

## [1.0.2] - 2026-02-10

- fixed: missing static/styles/output.css in whl/sdist

## [1.0.1post3] - 2026-02-09

- changed: dual-license either under MIT or Commerical License
- fixed: sidebars with wide content causes layout shift on hover when scollbars appear
- changed: lower Python dependency to 3.11 (instead of 3.13)

## [0.1.1] - 2026-02-02

- fix: Hide right sidebar button on mobile is not hidden if page has no subheadings.
- refactor: Replace Null's `display_local_toc` with Sphinx builtin `display_toc` Jinja context function to detect whether show a local ToC.

## [0.1.0] - 2026-01-23

Initial release.