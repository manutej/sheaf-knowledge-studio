#!/usr/bin/env python3
"""
VBM (Visual Browser Monitor) & Interactive UX Walkthrough Recorder (Round 6 / v6.0.0)
=====================================================================================
Launches a local HTTP server and headless Chromium via Playwright across:
  1. Desktop Viewport (1440 x 900, device_scale_factor=2)
  2. Mobile Viewport  (390 x 844 iPhone 14 Pro, device_scale_factor=2, is_mobile=True, has_touch=True)

Captures:
  - Full interactive video recordings (.webm) walking through Plates I–V, Visual Instruments,
    4-Act 10-Turn Podcast Player & Turn Rail, Plate IV 291/877 Declarations & 3D Alexandrov Poset,
    Plate V Cross-Corpus & Walkable Labs, Spivak Desktop Symbolic Sandbox, 1-Plate Focus Mode,
    Cream/Ink Theme, and Verbatim Page Reader with Anchored Formal Callouts.
  - 19 High-DPI PNG screenshots of every key state (saved to audits/vbm/ and Artifact Dir).
  - Programmatic DOM, Network & UX Ergonomics Telemetry (sticky header height % of viewport,
    horizontal overflow, SVG viewBox clipping, touch-target sizes, deferred bundle loading,
    failed network requests, 10-turn rail dot count, and zero raw LaTeX leaks).
"""
import functools
import http.server
import json
import os
import pathlib
import shutil
import socketserver
import threading
from playwright.sync_api import sync_playwright

REPO_DIR = pathlib.Path(__file__).resolve().parent.parent
WORKSPACE_DIR = REPO_DIR.parent
OUT_DIR = REPO_DIR / "audits" / "vbm"
ART_DIR = pathlib.Path("/Users/cairo/.gemini/antigravity/brain/109c7092-572c-4cbf-ac55-3677c5ef2652")
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def start_local_server(root_dir: pathlib.Path):
    handler = functools.partial(QuietHandler, directory=str(root_dir))
    httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)
    port = httpd.server_address[1]
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    return httpd, port


def collect_dom_ux_telemetry(page, label: str, failed_reqs: list) -> dict:
    dom_data = page.evaluate(
        """(label) => {
        const vw = window.innerWidth;
        const vh = window.innerHeight;
        const docScrollW = document.documentElement.scrollWidth;
        const horizontalOverflowPx = Math.max(0, docScrollW - vw);

        const ribbon = document.querySelector('.axis-ribbon');
        const ribbonRect = ribbon ? ribbon.getBoundingClientRect() : { height: 0 };
        const ribbonHeightPx = Math.round(ribbonRect.height);
        const ribbonViewportPct = Math.round((ribbonHeightPx / vh) * 1000) / 10;

        const dock = document.getElementById('mobileBottomDock');
        const dockRect = (dock && getComputedStyle(dock).display !== 'none')
            ? dock.getBoundingClientRect()
            : { height: 0 };
        const dockHeightPx = Math.round(dockRect.height);

        // Check visible buttons for touch target ergonomics (< 28px height)
        const visibleButtons = Array.from(document.querySelectorAll('button, .tab-card, .sym-btn, .inv-pill'))
            .filter(el => {
                const r = el.getBoundingClientRect();
                return r.width > 0 && r.height > 0 && getComputedStyle(el).visibility !== 'hidden';
            });
        const undersizedButtons = visibleButtons
            .filter(el => el.getBoundingClientRect().height < 28)
            .map(el => ({
                text: (el.textContent || '').trim().slice(0, 32),
                h: Math.round(el.getBoundingClientRect().height),
                w: Math.round(el.getBoundingClientRect().width),
                cls: el.className
            }));

        // Check visible SVGs for zero-size or horizontal clipping
        const svgs = Array.from(document.querySelectorAll('svg'))
            .filter(el => el.getBoundingClientRect().width > 0);
        const clippedSvgs = svgs.filter(el => {
            const r = el.getBoundingClientRect();
            return r.right > vw + 4 || r.width < 40 || r.height < 20;
        }).map(el => ({
            w: Math.round(el.getBoundingClientRect().width),
            h: Math.round(el.getBoundingClientRect().height),
            right: Math.round(el.getBoundingClientRect().right)
        }));

        // Check if any raw LaTeX backslashes are visible in text
        const bodyText = document.body.innerText || '';
        const rawLatexMatches = bodyText.match(/\\\\(mathcal|mathbf|xrightarrow|varprojlim|varinjlim|iota|pi|circ|sqcup)/g) || [];

        // Check deferred bundle & interactive state counts
        const allOpt = document.querySelector('#declKindSelect option[value="all"]');
        const allOptText = allOpt ? (allOpt.textContent || '').trim() : '';
        const turnRailDots = document.querySelectorAll('#podcastTurnRail .podcast-turn-dot').length;
        const atlasStateBtns = document.querySelectorAll('.atlas-state-bar .atlas-state-pill').length;
        const readerCalloutItems = document.querySelectorAll('#readerPageMeta .reader-formal-callout .rf-item').length;
        const walkableLabBtns = document.querySelectorAll('button[onclick*="__launchCourseModuleLab"]').length;

        return {
            label,
            viewport: `${vw}x${vh}`,
            docScrollW,
            horizontalOverflowPx,
            ribbonHeightPx,
            ribbonViewportPct,
            dockHeightPx,
            freeReadingViewportPct: Math.round(((vh - ribbonHeightPx - dockHeightPx) / vh) * 1000) / 10,
            visibleButtonCount: visibleButtons.length,
            undersizedButtonCount: undersizedButtons.length,
            undersizedButtonsSample: undersizedButtons.slice(0, 6),
            visibleSvgCount: svgs.length,
            clippedSvgCount: clippedSvgs.length,
            rawLatexLeakCount: rawLatexMatches.length,
            declAllOptionLabel: allOptText,
            turnRailDotCount: turnRailDots,
            atlasStatePillCount: atlasStateBtns,
            readerFormalCalloutCount: readerCalloutItems,
            walkableLabButtonCount: walkableLabBtns
        };
    }""",
        label,
    )
    dom_data["failedNetworkRequests"] = len(failed_reqs)
    dom_data["failedNetworkUrls"] = list(failed_reqs[:5])
    return dom_data


def save_shot(page, prefix: str, name: str, full_page: bool = False) -> str:
    fname = f"{prefix}_{name}.png"
    out_path = OUT_DIR / fname
    page.screenshot(path=str(out_path), full_page=full_page)
    if ART_DIR.exists():
        shutil.copy2(out_path, ART_DIR / fname)
    return fname


def attach_network_monitor(page, bucket: list):
    def _on_fail(req):
        err = req.failure or ""
        if req.resource_type == "media" and "ERR_ABORTED" in str(err):
            return
        bucket.append(f"FAIL:{req.url}")

    page.on("requestfailed", _on_fail)
    page.on(
        "response",
        lambda res: bucket.append(f"HTTP_{res.status}:{res.url}") if res.status >= 400 else None,
    )


def run_vbm_suite(phase_prefix: str = "r6_after"):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    httpd, port = start_local_server(REPO_DIR)
    base_url = f"http://127.0.0.1:{port}"
    marinov_url = f"{base_url}/studios/marinov-category-theory-illustrated/index.html"
    spivak_url = f"{base_url}/studios/spivak-category-theory-for-the-sciences/index.html"

    telemetry = []
    screenshots = []
    videos = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=CHROME_PATH if os.path.exists(CHROME_PATH) else None,
            headless=True,
        )

        # =====================================================================
        # 1. DESKTOP WALKTHROUGH & RECORDING (1440 x 900)
        # =====================================================================
        video_dir_desktop = OUT_DIR / f"video_{phase_prefix}_desktop"
        video_dir_desktop.mkdir(parents=True, exist_ok=True)
        ctx_desktop = browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=2,
            record_video_dir=str(video_dir_desktop),
            record_video_size={"width": 1440, "height": 900},
        )
        page = ctx_desktop.new_page()
        failed_desktop = []
        attach_network_monitor(page, failed_desktop)

        page.goto(marinov_url, wait_until="networkidle")
        page.wait_for_timeout(450)

        telemetry.append(collect_dom_ux_telemetry(page, f"{phase_prefix}_marinov_desktop_initial", failed_desktop))
        screenshots.append(save_shot(page, phase_prefix, "01_desktop_hero_and_plate1"))

        # Walk Instrument I-A: Espresso Machine & Polarity
        page.locator('#shifterTabs [data-shift="espresso"]').click()
        page.wait_for_timeout(300)
        page.locator('#shifterTabs').scroll_into_view_if_needed()
        screenshots.append(save_shot(page, phase_prefix, "02_desktop_plate1a_espresso_zoomout"))

        page.locator('#shifterTabs [data-shift="polarity"]').click()
        page.wait_for_timeout(300)
        screenshots.append(save_shot(page, phase_prefix, "03_desktop_plate1a_type_polarity"))

        # Walk Instrument I-B: Marinov's 6 Inkscape Visual Instruments + State Pills
        page.locator('#visualAtlasInstrument').scroll_into_view_if_needed()
        page.wait_for_timeout(250)
        page.locator('.atlas-state-bar .atlas-state-pill').nth(2).click()  # +240° (r₂) state!
        page.wait_for_timeout(250)
        screenshots.append(save_shot(page, phase_prefix, "04_desktop_plate1b_monoid_loops"))

        page.locator('#atlasTabs [data-atlas="hasse_cube"]').click()
        page.wait_for_timeout(300)
        page.locator('.atlas-state-bar .atlas-state-pill').nth(1).click()
        page.wait_for_timeout(250)
        screenshots.append(save_shot(page, phase_prefix, "05_desktop_plate1b_birkhoff_cube"))

        page.locator('#atlasTabs [data-atlas="heyting_lever"]').click()
        page.wait_for_timeout(300)
        screenshots.append(save_shot(page, phase_prefix, "06_desktop_plate1b_heyting_lever"))

        page.locator('#atlasTabs [data-atlas="russell_trees"]').click()
        page.wait_for_timeout(300)
        page.locator('.atlas-state-bar .atlas-state-pill').nth(2).click()
        page.wait_for_timeout(250)
        screenshots.append(save_shot(page, phase_prefix, "07_desktop_plate1b_russell_vs_trees"))

        page.locator('#atlasTabs [data-atlas="naturality_prism"]').click()
        page.wait_for_timeout(300)
        screenshots.append(save_shot(page, phase_prefix, "08_desktop_plate1b_naturality_prism"))

        # Walk Plate II: 6-World Rosetta Stone
        page.locator('#plate-2').scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        page.locator('#rosettaTabs [data-ros="product"]').click()
        page.wait_for_timeout(250)
        screenshots.append(save_shot(page, phase_prefix, "09_desktop_plate2_rosetta_stone"))

        # Walk Plate III: Sheaf Notebook + 4-Act 10-Turn Deep Dive Podcast & Turn Rail
        page.locator('#podcastStudioCard').scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        page.locator('#toggleTranscriptBtn').click()
        page.wait_for_timeout(250)
        page.locator('#podcastTurnRail .podcast-turn-dot').nth(5).click()
        page.wait_for_timeout(300)
        telemetry.append(collect_dom_ux_telemetry(page, f"{phase_prefix}_marinov_desktop_podcast_open", failed_desktop))
        screenshots.append(save_shot(page, phase_prefix, "10_desktop_plate3_4act_podcast_and_script"))

        # Walk Plate IV: 291 Declarations Browser & 3D Alexandrov Poset
        page.locator('#plate-4').scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        page.locator('[data-subview="declarations"]').click()
        page.wait_for_timeout(350)
        telemetry.append(collect_dom_ux_telemetry(page, f"{phase_prefix}_marinov_desktop_plate4_declarations", failed_desktop))
        screenshots.append(save_shot(page, phase_prefix, "12_desktop_plate4_declarations_291"))

        page.locator('[data-subview="atlas3d"]').click()
        page.wait_for_timeout(450)
        telemetry.append(collect_dom_ux_telemetry(page, f"{phase_prefix}_marinov_desktop_plate4_3d_poset", failed_desktop))
        screenshots.append(save_shot(page, phase_prefix, "13_desktop_plate4_3d_alexandrov_poset"))

        # Walk Plate V: Cross-Corpus Comparison & 7 Walkable Course Modules
        page.locator('#plate-5').scroll_into_view_if_needed()
        page.wait_for_timeout(350)
        telemetry.append(collect_dom_ux_telemetry(page, f"{phase_prefix}_marinov_desktop_plate5_course", failed_desktop))
        screenshots.append(save_shot(page, phase_prefix, "14_desktop_plate5_cross_corpus_and_labs"))

        # Walk 1-Plate Focus Mode + Dark Ink Theme + Verbatim Reader Drawer (p.14 with Formal Callouts)
        page.evaluate("window.__jumpToPage(14, 'Category')")
        page.wait_for_timeout(300)
        page.locator('[data-set-view="focus"]').click()
        page.wait_for_timeout(250)
        page.locator('[data-set-theme="dark"]').click()
        page.wait_for_timeout(350)
        telemetry.append(collect_dom_ux_telemetry(page, f"{phase_prefix}_marinov_desktop_focus_dark_reader", failed_desktop))
        screenshots.append(save_shot(page, phase_prefix, "11_desktop_focus_mode_dark_reader"))

        # Walk Spivak Desktop Plate III Symbolic Sandbox & 10-Turn Podcast Rail
        failed_spivak_desktop = []
        attach_network_monitor(page, failed_spivak_desktop)
        page.goto(spivak_url, wait_until="networkidle")
        page.wait_for_timeout(450)
        page.locator('#plate-3').scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        page.locator('#symSelector [data-sym="pullback"]').click()
        page.wait_for_timeout(300)
        telemetry.append(collect_dom_ux_telemetry(page, f"{phase_prefix}_spivak_desktop_plate3_sandbox", failed_spivak_desktop))
        screenshots.append(save_shot(page, phase_prefix, "15_desktop_spivak_plate3_symbolic_sandbox"))

        ctx_desktop.close()
        for vf in video_dir_desktop.glob("*.webm"):
            target_v = OUT_DIR / f"{phase_prefix}_desktop_walkthrough.webm"
            shutil.copy2(vf, target_v)
            if ART_DIR.exists():
                shutil.copy2(vf, ART_DIR / target_v.name)
            videos.append(target_v.name)

        # =====================================================================
        # 2. MOBILE WALKTHROUGH & RECORDING (390 x 844 iPhone 14 Pro)
        # =====================================================================
        video_dir_mobile = OUT_DIR / f"video_{phase_prefix}_mobile"
        video_dir_mobile.mkdir(parents=True, exist_ok=True)
        ctx_mobile = browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2,
            is_mobile=True,
            has_touch=True,
            record_video_dir=str(video_dir_mobile),
            record_video_size={"width": 390, "height": 844},
        )
        mpage = ctx_mobile.new_page()
        failed_mobile = []
        attach_network_monitor(mpage, failed_mobile)

        mpage.goto(marinov_url, wait_until="networkidle")
        mpage.wait_for_timeout(450)

        telemetry.append(collect_dom_ux_telemetry(mpage, f"{phase_prefix}_marinov_mobile_initial", failed_mobile))
        screenshots.append(save_shot(mpage, phase_prefix, "16_mobile_hero_and_sticky_header"))

        # Scroll to Instrument I-B on Mobile
        mpage.locator('#visualAtlasInstrument').scroll_into_view_if_needed()
        mpage.wait_for_timeout(350)
        telemetry.append(collect_dom_ux_telemetry(mpage, f"{phase_prefix}_marinov_mobile_visual_atlas", failed_mobile))
        screenshots.append(save_shot(mpage, phase_prefix, "17_mobile_visual_atlas_and_decoder"))

        # Scroll to Plate III Podcast & 10-Turn Rail on Mobile
        mpage.locator('#podcastStudioCard').scroll_into_view_if_needed()
        mpage.wait_for_timeout(350)
        telemetry.append(collect_dom_ux_telemetry(mpage, f"{phase_prefix}_marinov_mobile_podcast", failed_mobile))
        screenshots.append(save_shot(mpage, phase_prefix, "18_mobile_podcast_and_collapsed_cover"))

        # Test Spivak Studio on Mobile too
        failed_spivak_mobile = []
        attach_network_monitor(mpage, failed_spivak_mobile)
        mpage.goto(spivak_url, wait_until="networkidle")
        mpage.wait_for_timeout(400)
        mpage.locator('#podcastStudioCard').scroll_into_view_if_needed()
        mpage.wait_for_timeout(350)
        telemetry.append(collect_dom_ux_telemetry(mpage, f"{phase_prefix}_spivak_mobile_podcast", failed_spivak_mobile))
        screenshots.append(save_shot(mpage, phase_prefix, "19_mobile_spivak_podcast_studio"))

        ctx_mobile.close()
        for vf in video_dir_mobile.glob("*.webm"):
            target_v = OUT_DIR / f"{phase_prefix}_mobile_walkthrough.webm"
            shutil.copy2(vf, target_v)
            if ART_DIR.exists():
                shutil.copy2(vf, ART_DIR / target_v.name)
            videos.append(target_v.name)

        browser.close()

    httpd.shutdown()
    report = {
        "phase": phase_prefix,
        "screenshots": screenshots,
        "videos": videos,
        "telemetry": telemetry,
    }
    report_path = OUT_DIR / f"vbm_telemetry_{phase_prefix}.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    import sys
    phase = sys.argv[1] if len(sys.argv) > 1 else "r6_after"
    run_vbm_suite(phase)
