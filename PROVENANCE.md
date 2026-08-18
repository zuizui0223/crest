# CREST migration provenance

- Temporary source/host repository: `zuizui0223/mrm`
- Audited source commit copied to CREST: `72550fa8335cbffb901785f8a171c647b3cf8cc6`
- CREST migration merge: `6cc54e3d47fba2bc978c1c52d9028dbe56b8ea37`
- MRM extraction-completion merge: `5ed6b9183ca4eddca6e24d417191edd19700e666`
- Dedicated owner repository: `zuizui0223/crest`
- Status: **physical extraction complete**

The audited source snapshot contained J1–J7, O1, the J4/J7 NP-completeness boundary, analytic proof/control documents, the CREST philosophy manuscript, submission controls, and repository-hygiene corrections.

The dedicated CREST repository independently passed its theorem and obstruction tests on Python 3.10, 3.11, and 3.12; Python 3.12 also passed the philosophy submission verifier and repository-hygiene gate. After that verification, MRM removed the temporary `mrm/crest_*` modules, `test_crest_*` suite, CREST proofs/ledgers/manuscripts, and submission verifier. MRM now retains only one provenance pointer and its mechanism-robustness core.

Git history in MRM remains the pre-extraction provenance source and has not been rewritten.
