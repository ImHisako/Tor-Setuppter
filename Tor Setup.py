prefs = {
    "browser.security_level.security_slider": 1,
    "javascript.enabled": False,
    "app.update.auto": False,
    "browser.download.forbid_open_with": True,
    "browser.xul.error_pages.expert_bad_cert": True,
    "browser.cache.memory.enable": False,
    "browser.shell.shortcutFavicons": False,
    "browser.chrome.site_icons": False,
    "dom.storage.enabled": False,
    "webgl.disabled": True,
    "browser.display.use_document_fonts": 0,
    "gfx.downloadable_fonts.enabled": False,
    "gfx.font_rendering.graphite.enabled": False,
    "gfx.font_rendering.opentype_svg.enabled": False,
    "svg.disabled": True,
    "security.OCSP.enabled": 0,
    "permissions.default.camera": 2,
    "permissions.default.desktop-notification": 2,
    "permissions.default.geo": 2,
    "permissions.default.microphone": 2,
    "permissions.default.xr": 2,
    "network.IDN_show_punycode": True,
    "media.play-stand-alone": False,
    "media.autoplay.default": 5,
    "media.autoplay.blocking_policy": 2,
    "media.autoplay.block-event.enabled": True,
    "media.autoplay.allow-extension-background-pages": False,
    "network.websocket.max-connections": 0,
    "network.websocket.delay-failed-reconnects": False,
    "network.http.response.timeout": 1000,
    "network.http.sendRefererHeader": 1,
    "network.http.referer.XOriginPolicy": 1,
    "pdfjs.enabledCache.state": False,
    "pdfjs.handleOctetStream": False,
    "pdfjs.disabled": True,
    "pdfjs.disableAutoFetch": True,
    "pdfjs.disableFontFace": True,
    "pdfjs.disablePageLabels": True,
    "pdfjs.disableRange": True,
    "pdfjs.disableStream": True,
    "privacy.donottrackheader.enabled": False,
    "privacy.fingerprintingProtection": True,
    "privacy.trackingprotection.enabled": True,
    "privacy.trackingprotection.fingerprinting.enabled": True,
    "privacy.trackingprotection.pbmode.enabled": True,
    "privacy.trackingprotection.annotate_channels": True,
    "privacy.trackingprotection.socialtracking.enabled": True,
    "privacy.trackingprotection.cryptomining.enabled": True,
    "privacy.trackingprotection.emailtracking.enabled": True,
    "privacy.trackingprotection.emailtracking.pbmode.enabled": True,
    "privacy.trackingprotection.emailtracking.data_collection.enabled": False,
    "privacy.resistFingerprinting.spoofOsInUserAgentHeader": True,
    "privacy.socialtracking.block_cookies.enabled": True,
    "privacy.resistFingerprinting.pbmode": True,
    "privacy.resistFingerprinting.randomization.daily_reset.enabled": True,
    "privacy.resistFingerprinting.randomization.daily_reset.private.enabled": True,
    "privacy.spoof_english": 1,
    "media.webm.enabled": False,
    "media.mp4.enabled": False,
    "media.ogg.enabled": False,
    "media.wave.enabled": False,
    "media.flac.enabled": False,
    "media.opus.enabled": False,
    "media.ffmpeg.enabled": False,
    "media.encoder.webm.enabled": False,
    "media.gmp.decoder.enabled": False,
    "media.gmp.encoder.enabled": False,
    "media.mediasource.enabled": False,
    "media.media-capabilities.enabled": False
}

def bool_to_js(value):
    return "true" if value else "false"

def write_user_js(path="user.js"):
    with open(path, "w") as f:
        for key, value in prefs.items():
            if isinstance(value, bool):
                value_str = bool_to_js(value)
            elif isinstance(value, int):
                value_str = str(value)
            else:
                value_str = f'"{value}"'  # For string values if any
            f.write(f'user_pref("{key}", {value_str});\n')

if __name__ == "__main__":
    write_user_js()
    print("user.js created with Tor Browser security configuration.")
