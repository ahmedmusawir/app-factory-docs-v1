# QAM template installation proposal

DRAFT — source acceptance is settled; installation is pending. No destination file exists yet. AD-01 fixes the destination. Only the exact status/provenance translations below are proposed; no QA behavior changes, placeholder values, approvals, results or credentials are introduced. The immutable source snapshot must accompany the run. Accepted source version remains v0.3-draft; installed set is proposed as v0.3, governed by QAM_PLAYBOOK v1.0.

| Source relative path | Destination | Source SHA-256 | Expected installed SHA-256 after approved translations |
|---|---|---|---|
| AC_EVIDENCE_MATRIX.md | `03_BUILD_METHODOLOGY/_templates/QAM/AC_EVIDENCE_MATRIX.md` | ce619971ec58604e09f768de64337367cafec29ca30367b019e475c7ebf70883 | ce8ddf2b4aca084a088cfedc52242b218317b68f9fc27d226f1efdc589f4031b |
| AGENTS.md | `03_BUILD_METHODOLOGY/_templates/QAM/AGENTS.md` | 13c5be461a00bd6239da3b5a247bd91130c85dcf519da59b231fcc421e62eced | ffe3c85992415c52bead9366bbc8d97449f1b7d4f55195dfc99eb2fc1b905102 |
| AUTOMATION/README.md | `03_BUILD_METHODOLOGY/_templates/QAM/AUTOMATION/README.md` | 76d5fb29a0f2ee90e7281f091894e1f04c394a3cacea9606a5aa51438d5fcc45 | 943834f386a92130a5631a9d43e7b45cc079e868066f1e3a205c542f6d4f4457 |
| CLAUDE.md | `03_BUILD_METHODOLOGY/_templates/QAM/CLAUDE.md` | bf7d4ff22b5d8c14d8f370cc128bc23553a1d95ddb41545700e64a9d080ad535 | 034291d5e30a43e70ad096177cbfaf778b9db755ab1b833d8f3f6bf218fca8c2 |
| FINDINGS.md | `03_BUILD_METHODOLOGY/_templates/QAM/FINDINGS.md` | c17a149be9a6bea8aaac720c3de47ea9e7b5402bb86792b466c8e5a6f2156385 | 8d78800c60c588a633930ee063790e400c2d112d81b58ad9a7a2c8fee933e463 |
| GOVERNING/README.md | `03_BUILD_METHODOLOGY/_templates/QAM/GOVERNING/README.md` | b11da26e2793bd9bf816b51840f007922b3e4028a6298be7494e834ce28aee20 | 6e9eb64e857cc5fa39141c42e82f5687ffe9454e5cbbe18caa79b18ff502792b |
| HANDOFFS/ENGINEERING_HANDOFF.md | `03_BUILD_METHODOLOGY/_templates/QAM/HANDOFFS/ENGINEERING_HANDOFF.md` | ccb15192ecccfd1dceae95fa2e7f0b2fa6bd9e19f4956e1295964a89eaa7391f | f15edf39014449e9ef6415861a50b4a6347dc47481de723aa14e1d563c42540e |
| HANDOFFS/FILE_INDEX.template.json | `03_BUILD_METHODOLOGY/_templates/QAM/HANDOFFS/FILE_INDEX.template.json` | fa5705561225dc1b108c2e2173121f6949f0d9141d6b5010b577cb5d15e5e2fb | 417b97f9457043e6564e16d4203133425e63b69e9d3ad04fb8c499c59caa3771 |
| HANDOFFS/README.md | `03_BUILD_METHODOLOGY/_templates/QAM/HANDOFFS/README.md` | 82876906ba38d2d57506e934e645c38675768d5d76a66089b343d31273ecaba0 | adf319deff23b13a23a57009c0e2abff3902e6306394b489da1b30002d134ba2 |
| HANDOFFS/REVIEW_START_HERE.md | `03_BUILD_METHODOLOGY/_templates/QAM/HANDOFFS/REVIEW_START_HERE.md` | a7dc1fcac42b30ce6dd270078f5e9202d22aa011e2e531871acb0f5086d37633 | f1113b79eefd5f781e4d3cc9020e16ea000aca613a3fdb6622780faaf70c759b |
| PARENT_ENTRY_ROUTING.md | `03_BUILD_METHODOLOGY/_templates/QAM/PARENT_ENTRY_ROUTING.md` | 769345f5dc96fd52a654b65f663d51cacfa2ac65dd5b4f275afba01be9c38eb1 | 5a1494851d8646c00341871bb45403f3525917532a6bce80207afc5379f6b060 |
| QAM_APPROVAL.md | `03_BUILD_METHODOLOGY/_templates/QAM/QAM_APPROVAL.md` | caa2c0f8080bfdecdd48a5c11830ad3ea162c1dd309d87738045a63b58fa6538 | fea6762e15dc75f39f8af881173361c39759dcd5dad316a6b60ae1974d9ee07c |
| QAM_CERTIFICATION.md | `03_BUILD_METHODOLOGY/_templates/QAM/QAM_CERTIFICATION.md` | b2e7db8d3b27c064914bb30f269bd7ab46276eaef92ed3cfeb973c0abe144d19 | a4da44b7eb3d1377dadf5156193a254695f8ee59da80a0b81920f749e2074c83 |
| QAM_CLEANUP_REPORT.md | `03_BUILD_METHODOLOGY/_templates/QAM/QAM_CLEANUP_REPORT.md` | 0a2eb83607a81870031d96190263531afed26745fffc8218a3a004293c92a4c1 | c00550ac110825fa7ddb52a8727d0ac253c58d317f61794f8829928b51cc84ac |
| QAM_ENTRY.md | `03_BUILD_METHODOLOGY/_templates/QAM/QAM_ENTRY.md` | bc15f3c613a144be5a50c811752f00905a9585c6c4eb87300b7ee105da2c01fa | 226cc048fe55b8e67f8714d2bc75645bb676dd7927319d6a0910f061dac17c62 |
| QAM_EXECUTION_REPORT.md | `03_BUILD_METHODOLOGY/_templates/QAM/QAM_EXECUTION_REPORT.md` | 723afabf776deddae595dfda5f1bca70dfc2c5616da32fe63de9dcf45e5b7177 | b9cf409e6465b5039359eed6a92364e67eed6c3efb80ddb0383b6457c0c5627b |
| QAM_MANIFEST.md | `03_BUILD_METHODOLOGY/_templates/QAM/QAM_MANIFEST.md` | 2dc5ebb4dd8d257047b4f72b53122ad67953372106ddb7f2662a6858c5948c62 | 36f5a489f9f598800d82d9fc650f76dd3730d4db5bd013a0cf9054d1782791e4 |
| QAM_PACKAGING.md | `03_BUILD_METHODOLOGY/_templates/QAM/QAM_PACKAGING.md` | 1a9a61ae19b2ee98cc481368d46ec0403895225f51afaec293e440d3ccc84ea7 | d93dba4a677997bf9344e969615a01244648bcf9176ea531068cb2f0fcf475e3 |
| QAM_PREFLIGHT.md | `03_BUILD_METHODOLOGY/_templates/QAM/QAM_PREFLIGHT.md` | a887e728a817b51944583c30d89a285820fb680c80c2568459ba32ea374f97c6 | cd870cf83ab7dd91fed171176b9a5d351092dc0db6b347ff87732b6c1a96c9de |
| QAM_RECON_REPORT.md | `03_BUILD_METHODOLOGY/_templates/QAM/QAM_RECON_REPORT.md` | 977fb2630ac38727936abc0770e748a705d377b31850a875beb841563eb9b764 | 29db40e71121b8b4693e1c1ea0ff81a134d8c837e42ded94fc15870b8cc83457 |
| QAM_RISK_REQUIREMENTS.md | `03_BUILD_METHODOLOGY/_templates/QAM/QAM_RISK_REQUIREMENTS.md` | 6e8cfb4e2df064b5eb8c2402654b66dec774b10c173a76134c04c65e854a4d76 | d617c02d038f0c152093b45a8439b9e3e6a59245e9ce87c10c791c28cc6139dc |
| QAM_STATE.md | `03_BUILD_METHODOLOGY/_templates/QAM/QAM_STATE.md` | 487b60e8bb7c45f1f246fa9d22e276a6498b1fdd2ddb90fd99d847e8a6d78a1e | 59821844737c25872067337d5c5d35e66d2b699a29950fc64544a6d161a28e9c |
| QAM_TEST_PLAN.md | `03_BUILD_METHODOLOGY/_templates/QAM/QAM_TEST_PLAN.md` | 2df20cbd259a76d4bb58759478c30ce21e2774cfff64e8a796b142c1e7020dc7 | d855ad6d09c9a1d5d6e2601ea4c03898a5261a28e6820f49e53b7d4170dbbb6d |
| README.md | `03_BUILD_METHODOLOGY/_templates/QAM/README.md` | 8ccc80f3f2f89549bd4a29260f236a33fe4eee5b3f08933ca62fb08e5bcbd0c3 | 8753f7bf66634856c4439052ba1633d9cef2d15eea0b5fe1b4497925fb0707b1 |
| evidence/README.md | `03_BUILD_METHODOLOGY/_templates/QAM/evidence/README.md` | 385ad08e235c77b50a62ab78c5976e00df4f2167fc40f814f0300646a532d6df | d31808111027bb0551c0a43dd3776a51eef9e3c5a813a623b98d3c0cfb7b3be6 |

## Exact translation authority

`TEMPLATE_INSTALL_PLAN.json` enumerates every old/new span and expected count per file. Recompute destination hashes after installation; never claim byte identity to the source after relabeling. Internal module-relative placeholders are not Hub links and remain unchanged. The provenance source filename identifies the preserved input.

## Required installation checks (Engineer then independent QA)

1. Exact 25-file destination set and source manifest membership; no missing or extra files.
2. Each source SHA matches the accepted package; each installed SHA matches the approved transformed bytes.
3. CLAUDE.md and AGENTS.md routing bodies remain byte-identical and assign QA Executor; parent routing still separates Engineering from QA.
4. AM-1 exact cleanup column, AM-2 exact STOP cell, AM-3 command/cwd/exit/unfiltered output, and all eleven adopted SR rows remain unchanged.
5. Nineteen-state vocabulary matches dispatch rows; READY FOR ENGINEERING is initial; REPAIR RULED — AWAITING COMMIT remains a waiting state distinct from RELEASED FOR Q4. Unknown state routes to discrepancy and next owner.
6. Owner/writable-lane/permission tables agree. No populated result, approval, certificate, candidate SHA, credential or production target. Source provenance hash is not a candidate SHA.
7. Parent-contract references, local governing source provenance and snapshot links resolve after the snapshot is committed.
8. Enumerate template checks explicitly in the independent acceptance spec: current lints do not recurse here. No template exporter, validator, runtime dispatcher or browser adapter is delivered by this installation.

These are proposed installation verifications, not a fresh acceptance review of Fable’s already accepted QA behavior.
