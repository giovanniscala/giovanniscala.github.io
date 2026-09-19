#!/usr/bin/env python3
"""Generate the canonical publication catalogue for giovanniscala.github.io.

The ledger is intentionally stored as structured data here so that visible
publication pages and BibTeX records cannot silently drift apart.
"""

from __future__ import annotations

import json
import shutil
import tempfile
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS_DIR = ROOT / "content" / "publication"


def entry(**kwargs):
    return kwargs


PUBLICATIONS = [
    entry(kind="journal", year=2026, date="2026-06-29", slug="finite-size-security-qkd",
          key="Staffieri2026FiniteSizeProofs", title="Finite-size security of QKD: comparison of three proof techniques",
          authors=["Gabriele Staffieri", "Giovanni Scala", "Cosmo Lupo"],
          venue="European Physical Journal Plus", short="Eur. Phys. J. Plus", volume="141", pages="754",
          doi="10.1140/epjp/s13360-026-07915-y", arxiv="2601.03829",
          tags=["Quantum key distribution", "Finite-size security"]),
    entry(kind="journal", year=2026, date="2026-02-24", slug="finite-size-secret-key-rates-dm-cvqkd",
          key="Staffieri2026FiniteSizeCVQKD", title="Finite-size secret-key rates of discrete modulation continuous-variable quantum key distribution under Gaussian attacks",
          authors=["Gabriele Staffieri", "Giovanni Scala", "Cosmo Lupo"],
          venue="Physical Review A", short="Phys. Rev. A", volume="113", pages="022445",
          doi="10.1103/rwq3-p1m6", arxiv="2509.14345",
          tags=["Quantum key distribution", "Continuous variables", "Finite-size security"]),
    entry(kind="journal", year=2026, date="2025-12-09", slug="entanglement-third-order-randomized-measurements",
          key="Scala2026ThirdOrderInvariants", title="Entanglement detection via third-order local invariants from randomized measurements",
          authors=["Giovanni Scala", "Anindita Bera", "Gniewomir Sarbicki"],
          venue="Quantum Science and Technology", short="Quantum Sci. Technol.", volume="11", pages="015022",
          doi="10.1088/2058-9565/ae1d4b", arxiv="2506.18303", featured=True,
          summary="Local-unitary invariants provide an experimentally accessible route to entanglement detection from randomized measurements.",
          tags=["Entanglement", "Randomized measurements", "Local invariants"]),
    entry(kind="journal", year=2025, date="2025-09-01", slug="future-secure-communications-diqkd",
          key="Ghoreishi2025FutureSecureCommunications", title="The future of secure communications: device independence in quantum key distribution",
          authors=["Seyed Arash Ghoreishi", "Giovanni Scala", "Renato Renner", "Letícia Lira Tacca", "Jan Bouda", "Stephen Patrick Walborn", "Marcin Pawłowski"],
          venue="Physics Reports", short="Phys. Rep.", volume="1149", pages="1--97",
          doi="10.1016/j.physrep.2025.09.006", arxiv="2504.06350", featured=True,
          summary="A review connecting device-independent security proofs, nonlocality, and the experimental challenges of quantum key distribution.",
          tags=["Quantum key distribution", "Device independence", "Review"]),
    entry(kind="journal", year=2025, date="2025-10-14", slug="optimal-robust-error-filtration",
          key="Ali2025ErrorFiltration", title="Optimal and robust error filtration for quantum information processing",
          authors=["Aaqib Ali", "Giovanni Scala", "Cosmo Lupo"],
          venue="Physical Review A", short="Phys. Rev. A", volume="112", pages="042418",
          doi="10.1103/534r-kp3z", arxiv="2409.01398", featured=True,
          summary="Optimized probabilistic error filtration for quantum information processing and sensing under realistic noise.",
          tags=["Error filtration", "Error mitigation", "Quantum information"]),
    entry(kind="journal", year=2025, date="2025-06-01", slug="self-testing-tilted-strategies",
          key="Gigena2025SelfTesting", title="Self-testing tilted strategies for maximal loophole-free nonlocality",
          authors=["Nicolas Gigena", "Ekta Panwar", "Giovanni Scala", "Mateus Araújo", "Máté Farkas", "Anubhav Chaturvedi"],
          venue="npj Quantum Information", short="npj Quantum Inf.", volume="11", pages="82",
          doi="10.1038/s41534-025-01029-6", arxiv="2405.08743", featured=True,
          summary="Self-testing of doubly tilted CHSH strategies relevant to Bell experiments with inefficient detectors.",
          tags=["Self-testing", "Bell nonlocality", "Device independence"]),
    entry(kind="journal", year=2025, date="2024-03-18", slug="generalizing-choi-map-m3",
          key="Bera2025GeneralizingChoi", title="Generalizing Choi map in M3 beyond circulant scenario",
          authors=["Anindita Bera", "Giovanni Scala", "Gniewomir Sarbicki", "Dariusz Chruściński"],
          venue="Linear and Multilinear Algebra", short="Linear Multilinear Algebra", volume="73", issue="2", pages="177--192",
          doi="10.1080/03081087.2024.2326249",
          aliases=["/publication/2030-preprint/10-05-2023_arx/"],
          tags=["Positive maps", "Entanglement witnesses", "Choi map"]),
    entry(kind="journal", year=2024, date="2024-11-01", slug="chaotic-light-correlation-imaging-turbulence",
          key="Scala2024ImagingTurbulence", title="Robustness of chaotic-light correlation imaging against turbulence",
          authors=["Giovanni Scala", "Gianlorenzo Massaro", "Germano Borreggine", "Cosmo Lupo", "Milena D’Angelo", "Francesco V. Pepe"],
          venue="European Physical Journal Plus", short="Eur. Phys. J. Plus", volume="139", pages="1010",
          doi="10.1140/epjp/s13360-024-05769-w", arxiv="2501.01967",
          tags=["Quantum imaging", "Turbulence", "Correlation imaging"]),
    entry(kind="journal", year=2024, date="2024-04-26", slug="optimality-generalized-choi-maps-m3",
          key="Scala2024OptimalityChoi", title="Optimality of generalized Choi maps in M3",
          authors=["Giovanni Scala", "Anindita Bera", "Gniewomir Sarbicki", "Dariusz Chruściński"],
          venue="Journal of Physics A: Mathematical and Theoretical", short="J. Phys. A", volume="57", pages="195301",
          doi="10.1088/1751-8121/ad3ca6", arxiv="2312.02814",
          tags=["Positive maps", "Entanglement witnesses", "Choi map"]),
    entry(kind="journal", year=2024, date="2024-02-21", slug="hyperbit-theory-limitations",
          key="Scala2024Hyperbit", title="Advantages of quantum communication revealed by the reexamination of hyperbit theory limitations",
          authors=["Giovanni Scala", "Seyed Arash Ghoreishi", "Marcin Pawłowski"],
          venue="Physical Review A", short="Phys. Rev. A", volume="109", pages="022230",
          doi="10.1103/PhysRevA.109.022230", arxiv="2308.16114",
          tags=["Quantum communication", "Hyperbits", "Quantum advantage"]),
    entry(kind="journal", year=2024, date="2024-01-12", slug="contextuality-bell-random-two-qubit",
          key="Scala2024ContextualityBell", title="Insights into Quantum Contextuality and Bell Nonclassicality: a Study on Random Pure Two-Qubit Systems",
          authors=["Giovanni Scala", "Antonio Mandarino"],
          venue="International Journal of Theoretical Physics", short="Int. J. Theor. Phys.", volume="63", pages="17",
          doi="10.1007/s10773-023-05543-1", arxiv="2310.09047",
          tags=["Contextuality", "Bell nonlocality", "Random states"]),
    entry(kind="journal", year=2023, date="2023-08-10", slug="genuinely-nonclassical-interference",
          key="Catani2023Interference", title="Aspects of the phenomenology of interference that are genuinely nonclassical",
          authors=["Lorenzo Catani", "Matthew Leifer", "Giovanni Scala", "David Schmid", "Robert W. Spekkens"],
          venue="Physical Review A", short="Phys. Rev. A", volume="108", pages="022207",
          doi="10.1103/PhysRevA.108.022207", arxiv="2211.09850",
          aliases=["/publication/2030-preprint/06_06_2023_prxq/"],
          tags=["Contextuality", "Interference", "Quantum foundations"]),
    entry(kind="journal", year=2023, date="2023-07-01", slug="local-set-chsh-bell",
          key="Gigena2023LocalSet", title="Revisited aspects of the local set in CHSH Bell scenario",
          authors=["Nicolas Gigena", "Giovanni Scala", "Antonio Mandarino"],
          venue="International Journal of Quantum Information", short="Int. J. Quantum Inf.", volume="21", issue="7", pages="2340005",
          doi="10.1142/S0219749923400051", arxiv="2302.06320",
          aliases=["/publication/2023/02_02_2023_ijqi/"], tags=["Bell inequalities", "CHSH", "Local polytope"]),
    entry(kind="journal", year=2023, date="2023-01-06", slug="fidelity-robustness-chsh-bell",
          key="Mandarino2023FidelityRobustness", title="On the Fidelity Robustness of CHSH–Bell Inequality via Filtered Random States",
          authors=["Antonio Mandarino", "Giovanni Scala"],
          venue="Entropy", short="Entropy", volume="25", issue="1", pages="94",
          doi="10.3390/e25010094", arxiv="2310.09231",
          aliases=["/publication/2023/04_01_2023_entropy/"], tags=["Bell inequalities", "CHSH", "Fidelity"]),
    entry(kind="journal", year=2022, date="2022-12-07", slug="nonclassical-uncertainty-relations",
          key="Catani2022Uncertainty", title="What is Nonclassical about Uncertainty Relations?",
          authors=["Lorenzo Catani", "Matthew Leifer", "Giovanni Scala", "David Schmid", "Robert W. Spekkens"],
          venue="Physical Review Letters", short="Phys. Rev. Lett.", volume="129", pages="240401",
          doi="10.1103/PhysRevLett.129.240401", arxiv="2207.11779", featured=True,
          summary="The functional form of uncertainty relations can witness contextuality under an operational symmetry condition.",
          aliases=["/publication/2022/09_12_2022_prl/", "/publication/2022/31_07_2022_arx/"],
          assets={"content/publication/2022/09_12_2022_prl/Poster_Singapore.pdf":"Poster_Singapore.pdf",
                  "content/publication/2022/09_12_2022_prl/slides.pdf":"slides.pdf",
                  "content/publication/2022/09_12_2022_prl/Gdansk_3Aug2022.pptx":"Gdansk_3Aug2022.pptx"},
          url_poster="Poster_Singapore.pdf", url_slides="slides.pdf",
          tags=["Contextuality", "Uncertainty relations", "Quantum foundations"]),
    entry(kind="journal", year=2022, date="2022-10-01", slug="correlation-plenoptic-imaging-snr",
          key="Massaro2022ComparativeSNR", title="Comparative analysis of signal-to-noise ratio in correlation plenoptic imaging architectures",
          authors=["Gianlorenzo Massaro", "Giovanni Scala", "Milena D’Angelo", "Francesco V. Pepe"],
          venue="European Physical Journal Plus", short="Eur. Phys. J. Plus", volume="137", pages="1123",
          doi="10.1140/epjp/s13360-022-03295-1", arxiv="2206.13412",
          aliases=["/publication/2022/31_06_2022_epjp/"], tags=["Correlation imaging", "Signal-to-noise ratio", "Quantum imaging"]),
    entry(kind="journal", year=2022, date="2022-09-01", slug="generalising-bell-inequalities",
          key="Karczewski2022BellInequalities", title="Avenues to generalising Bell inequalities",
          authors=["Marcin Karczewski", "Giovanni Scala", "Antonio Mandarino", "Ana Belén Sainz", "Marek Żukowski"],
          venue="Journal of Physics A: Mathematical and Theoretical", short="J. Phys. A", volume="55", pages="384011",
          doi="10.1088/1751-8121/ac8a28", arxiv="2202.06606",
          aliases=["/publication/2022/01_08_2022_jpa/"], tags=["Bell inequalities", "Nonlocality"]),
    entry(kind="journal", year=2022, date="2022-06-01", slug="thermal-light-distance-sensitivity",
          key="Pepe2022DistanceSensitivity", title="Distance sensitivity of thermal light second-order interference beyond spatial coherence",
          authors=["Francesco V. Pepe", "Giovanni Scala", "Gabriele Chilleri", "Danilo Triggiani", "Yoon-Ho Kim", "Vincenzo Tamma"],
          venue="European Physical Journal Plus", short="Eur. Phys. J. Plus", volume="137", pages="647",
          doi="10.1140/epjp/s13360-022-02857-7", arxiv="2011.05224",
          aliases=["/publication/2022/01_06_2022_epjp/"], tags=["Second-order interference", "Thermal light", "Metrology"]),
    entry(kind="journal", year=2021, date="2021-06-01", slug="correlation-tensor-case-study",
          key="Sarbicki2021DetectionPower", title="Detection power of separability criteria based on a correlation tensor: a case study",
          authors=["Gniewomir Sarbicki", "Giovanni Scala", "Dariusz Chruściński"],
          venue="Open Systems & Information Dynamics", short="Open Syst. Inf. Dyn.", volume="28", issue="2", pages="2150010",
          doi="10.1142/S1230161221500104", aliases=["/publication/2021/04_11_2021_osid/"],
          tags=["Entanglement", "Separability criteria", "Correlation tensors"]),
    entry(kind="journal", year=2021, date="2021-07-01", slug="beyond-rabi-model",
          key="Scala2021BeyondRabi", title="Beyond the Rabi model: Light interactions with polar atomic systems in a cavity",
          authors=["Giovanni Scala", "Karolina Słowik", "Paolo Facchi", "Saverio Pascazio", "Francesco V. Pepe"],
          venue="Physical Review A", short="Phys. Rev. A", volume="104", pages="013722",
          doi="10.1103/PhysRevA.104.013722", aliases=["/publication/2021/04_30_2021_pra/"],
          tags=["Light-matter interaction", "Cavity QED", "Rabi model"]),
    entry(kind="journal", year=2020, date="2020-12-30", slug="extended-quantum-systems-dispersive-media",
          key="Scala2020DispersiveMedia", title="Light interaction with extended quantum systems in dispersive media",
          authors=["Giovanni Scala", "Francesco V. Pepe", "Paolo Facchi", "Saverio Pascazio", "Karolina Słowik"],
          venue="New Journal of Physics", short="New J. Phys.", volume="22", pages="123047",
          doi="10.1088/1367-2630/abd204", aliases=["/publication/2020/12_30_2020_njp/"],
          assets={"content/publication/2020/12_30_2020_njp/poster.pptx":"poster.pptx"}, url_poster="poster.pptx",
          tags=["Light-matter interaction", "Quantum optics", "Dispersive media"]),
    entry(kind="journal", year=2020, date="2020-10-21", slug="enhanced-realignment-criterion",
          key="Sarbicki2020Realignment", title="Enhanced realignment criterion vs linear entanglement witnesses",
          authors=["Gniewomir Sarbicki", "Giovanni Scala", "Dariusz Chruściński"],
          venue="Journal of Physics A: Mathematical and Theoretical", short="J. Phys. A", volume="53", pages="455302",
          doi="10.1088/1751-8121/abba46", aliases=["/publication/2020/10_21_2020_jpa/"],
          assets={"content/publication/2020/10_21_2020_jpa/featured.PNG":"featured.png"},
          tags=["Entanglement", "Realignment criterion", "Entanglement witnesses"]),
    entry(kind="journal", year=2020, date="2020-02-01", slug="multipartite-correlation-tensor",
          key="Sarbicki2020CorrelationTensor", title="Family of multipartite separability criteria based on a correlation tensor",
          authors=["Gniewomir Sarbicki", "Giovanni Scala", "Dariusz Chruściński"],
          venue="Physical Review A", short="Phys. Rev. A", volume="101", pages="012341",
          doi="10.1103/PhysRevA.101.012341", aliases=["/publication/2020/01_22_2020_pra/"],
          assets={"content/publication/2020/01_22_2020_pra/2020_pra_poster.pdf":"2020_pra_poster.pdf",
                  "content/publication/2020/01_22_2020_pra/2020_pra_slides.pdf":"2020_pra_slides.pdf"},
          url_poster="2020_pra_poster.pdf", url_slides="2020_pra_slides.pdf",
          tags=["Entanglement", "Separability criteria", "Correlation tensors"]),
    entry(kind="journal", year=2019, date="2019-05-07", slug="correlation-plenoptic-imaging-chaotic-light",
          key="Scala2019PlenopticImaging", title="Signal-to-noise properties of correlation plenoptic imaging with chaotic light",
          authors=["Giovanni Scala", "Milena D’Angelo", "Augusto Garuccio", "Saverio Pascazio", "Francesco V. Pepe"],
          venue="Physical Review A", short="Phys. Rev. A", volume="99", pages="053808",
          doi="10.1103/PhysRevA.99.053808", arxiv="1901.11075",
          aliases=["/publication/2019/05_07_2019_pra/", "/publication/2019/05_07_2020_pra/"],
          assets={"content/publication/2019/05_07_2019_pra/CPI_snr_poster.pdf":"CPI_snr_poster.pdf",
                  "content/publication/2019/05_07_2019_pra/CPM_SPIE_PE_2020.pptx":"CPM_SPIE_PE_2020.pptx"},
          url_poster="CPI_snr_poster.pdf", url_slides="CPM_SPIE_PE_2020.pptx",
          tags=["Correlation plenoptic imaging", "Quantum imaging", "Signal-to-noise ratio"]),
    entry(kind="conference", year=2022, date="2022-05-01", slug="interactions-polar-quantum-systems-light",
          key="Slowik2022PolarSystems", title="Interactions of polar quantum systems with light",
          authors=["Karolina Słowik", "Piotr Gładysz", "Giovanni Scala", "Piotr Wcisło", "Francesco V. Pepe", "Paolo Facchi", "Saverio Pascazio"],
          venue="CLEO: Applications and Technology", short="CLEO", pages="JTu3A.1",
          external="https://opg.optica.org/viewmedia.cfm?seq=0&uri=cleo_at-2022-JTu3A.1",
          tags=["Light-matter interaction", "Quantum optics"]),
    entry(kind="conference", year=2020, date="2020-04-01", slug="signal-to-noise-ratio-correlation-plenoptic-imaging",
          key="Scala2020SPIE", title="Signal-to-noise ratio in correlation plenoptic imaging",
          authors=["Giovanni Scala", "Gianlorenzo Massaro", "Milena D’Angelo", "Augusto Garuccio", "Saverio Pascazio", "Francesco V. Pepe"],
          venue="Proceedings of SPIE", short="Proc. SPIE", volume="11347", pages="1134713",
          doi="10.1117/12.2555701", tags=["Correlation plenoptic imaging", "Quantum imaging"]),
    entry(kind="conference", year=2019, date="2019-01-01", slug="two-level-broken-inversion-symmetry",
          key="Scala2019BrokenInversion", title="Two-Level Systems with Broken Inversion Symmetry",
          authors=["Giovanni Scala"], venue="Proceedings", short="Proceedings", volume="12", pages="49",
          doi="10.3390/proceedings2019012049", tags=["Light-matter interaction", "Two-level systems"]),
    entry(kind="preprint", year=2026, date="2026-08-26", slug="recovery-free-chsh-particle-loss",
          key="Scala2026ParticleLoss", title="Recovery-Free CHSH Nonlocality with Particle Loss",
          authors=["Giovanni Scala", "Cosmo Lupo"], arxiv="2608.26407",
          tags=["Bell nonlocality", "Particle loss", "CHSH"]),
    entry(kind="preprint", year=2026, date="2026-04-14", slug="third-order-local-randomized-finite-size",
          key="Scala2026FiniteSizeEntanglement", title="Third-Order Local Randomized Measurements for Finite-size Entanglement Certification",
          authors=["Giovanni Scala", "Corrado Cosimo Mattiacci", "Dorota Pietryka", "Gniewomir Sarbicki"], arxiv="2604.13165",
          tags=["Entanglement", "Randomized measurements", "Finite-size certification"]),
    entry(kind="preprint", year=2026, date="2026-03-19", slug="preprocessing-noise-finite-size-qkd",
          key="Staffieri2026PreprocessingNoise", title="Preprocessing noise in finite-size quantum key distribution",
          authors=["Gabriele Staffieri", "Giuseppe D’Ambruoso", "Giovanni Scala", "Cosmo Lupo"], arxiv="2603.18213",
          tags=["Quantum key distribution", "Finite-size security", "Noise"]),
    entry(kind="preprint", year=2026, date="2026-03-19", slug="finite-size-resource-scaling-qml",
          key="Ali2026FiniteSizeQML", title="Finite-size resource scaling for learning quantum phase transitions with fidelity-based support vector machines",
          authors=["Aaqib Ali", "Giovanni Scala", "Cosmo Lupo", "Antonio Mandarino"], arxiv="2603.18211",
          tags=["Quantum machine learning", "Quantum phase transitions", "Finite-size scaling"]),
    entry(kind="preprint", year=2023, date="2023-08-15", slug="information-theoretical-entanglement-witnesses",
          key="Cavalcanti2023EntanglementWitnesses", title="Information theoretical perspective on the method of Entanglement Witnesses",
          authors=["Paulo J. Cavalcanti", "Giovanni Scala", "Antonio Mandarino", "Cosmo Lupo"], arxiv="2308.07744",
          tags=["Entanglement witnesses", "Information theory", "Entanglement"]),
]


TYPE_CODE = {"conference": "1", "journal": "2", "preprint": "3"}


def q(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def publication_label(item: dict) -> str:
    if item["kind"] == "preprint":
        return f"arXiv:{item['arxiv']} ({item['year']})"
    bits = [item["venue"]]
    if item.get("volume"):
        bits.append(item["volume"])
    if item.get("issue"):
        bits[-1] += f"({item['issue']})"
    if item.get("pages"):
        bits.append(item["pages"])
    return ", ".join(bits) + f" ({item['year']})"


def render_front_matter(item: dict) -> str:
    lines = ["---", f"title: {q(item['title'])}", "authors:"]
    for author in item["authors"]:
        lines.append(f"- {q('admin' if author == 'Giovanni Scala' else author)}")
    lines += [
        f"date: {q(item['date'] + 'T00:00:00Z')}",
        f"publishDate: {q(item['date'] + 'T00:00:00Z')}",
        f"publication_types: [{q(TYPE_CODE[item['kind']])}]",
        f"publication: {q(publication_label(item))}",
        f"publication_short: {q(item.get('short', item.get('venue', 'Preprint')))}",
        f"publication_status: {q({'journal': 'published', 'conference': 'conference/proceedings', 'preprint': 'preprint'}[item['kind']])}",
    ]
    if item.get("doi"):
        lines.append(f"doi: {q(item['doi'])}")
    if item.get("summary"):
        lines.append(f"summary: {q(item['summary'])}")
    lines.append("tags:")
    lines.extend(f"- {q(tag)}" for tag in item.get("tags", []))
    lines.append(f"featured: {'true' if item.get('featured') else 'false'}")
    if item.get("aliases"):
        lines.append("aliases:")
        lines.extend(f"- {q(alias)}" for alias in item["aliases"])
    if item.get("arxiv"):
        lines.append(f"url_pdf: {q('https://arxiv.org/pdf/' + item['arxiv'])}")
    if item.get("url_poster"):
        lines.append(f"url_poster: {q(item['url_poster'])}")
    if item.get("url_slides"):
        lines.append(f"url_slides: {q(item['url_slides'])}")
    if item.get("external"):
        lines += ["links:", "- name: Proceedings", f"  url: {q(item['external'])}"]
    lines.append("---")
    return "\n".join(lines) + "\n"


def bibtex(item: dict) -> str:
    kind = "article" if item["kind"] == "journal" else "inproceedings" if item["kind"] == "conference" else "misc"
    fields = [
        ("author", " and ".join(item["authors"])),
        ("title", "{" + item["title"] + "}"),
        ("year", str(item["year"])),
    ]
    if item["kind"] == "journal":
        fields.append(("journal", item["venue"].replace("&", r"\&")))
    elif item["kind"] == "conference":
        fields.append(("booktitle", item["venue"].replace("&", r"\&")))
    if item.get("volume"):
        fields.append(("volume", item["volume"]))
    if item.get("issue"):
        fields.append(("number", item["issue"]))
    if item.get("pages"):
        fields.append(("pages", item["pages"]))
    if item.get("doi"):
        fields.append(("doi", item["doi"]))
        fields.append(("url", "https://doi.org/" + item["doi"]))
    elif item.get("arxiv"):
        fields += [("eprint", item["arxiv"]), ("archivePrefix", "arXiv"), ("primaryClass", "quant-ph"),
                   ("url", "https://arxiv.org/abs/" + item["arxiv"])]
    elif item.get("external"):
        fields.append(("url", item["external"]))
    body = ",\n".join(f"  {name} = {{{value}}}" for name, value in fields)
    return f"@{kind}{{{item['key']},\n{body}\n}}\n"


def main() -> None:
    counts = Counter(item["kind"] for item in PUBLICATIONS)
    assert counts == Counter({"journal": 24, "conference": 3, "preprint": 5}), counts
    assert all(item.get("arxiv") != "2609.08635" for item in PUBLICATIONS)
    assert len({item["slug"] for item in PUBLICATIONS}) == len(PUBLICATIONS)

    with tempfile.TemporaryDirectory(prefix="publication-assets-") as temp_name:
        temp = Path(temp_name)
        saved_assets: dict[tuple[str, str], Path] = {}
        for item in PUBLICATIONS:
            for old_rel, new_name in item.get("assets", {}).items():
                # On the first run, assets live at the legacy path. On later
                # runs, preserve them from the generated canonical folder so
                # publication generation remains idempotent.
                legacy_source = ROOT / old_rel
                canonical_source = PUBLICATIONS_DIR / str(item["year"]) / item["slug"] / new_name
                source = legacy_source if legacy_source.exists() else canonical_source
                if source.exists():
                    target = temp / item["slug"] / new_name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, target)
                    saved_assets[(item["slug"], new_name)] = target

        if PUBLICATIONS_DIR.exists():
            shutil.rmtree(PUBLICATIONS_DIR)
        PUBLICATIONS_DIR.mkdir(parents=True)
        (PUBLICATIONS_DIR / "_index.md").write_text(
            "---\n"
            "title: Publications\n"
            "summary: Peer-reviewed articles, active preprints, and conference proceedings.\n"
            "date: 2026-09-18\n"
            "cms_exclude: true\n"
            "view: 4\n"
            "---\n\n"
            "This catalogue contains 24 peer-reviewed journal articles, five active preprints, and three conference or proceedings contributions. "
            "Use the publication-type filter to browse each category.\n",
            encoding="utf-8",
        )

        for item in PUBLICATIONS:
            folder = PUBLICATIONS_DIR / str(item["year"]) / item["slug"]
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "index.md").write_text(render_front_matter(item), encoding="utf-8")
            (folder / "cite.bib").write_text(bibtex(item), encoding="utf-8")
            for new_name in item.get("assets", {}).values():
                saved = saved_assets.get((item["slug"], new_name))
                if saved:
                    shutil.copy2(saved, folder / new_name)

    print(f"Generated {len(PUBLICATIONS)} records: {dict(counts)}")


if __name__ == "__main__":
    main()
