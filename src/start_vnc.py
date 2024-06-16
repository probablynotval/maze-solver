import atexit
import logging
import os
import signal
import subprocess
import sys

from config import load_config


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)


def setup_vnc():
    config = load_config()
    window_width = config["window"]["width"]
    window_height = config["window"]["height"]
    display = ":1"

    os.environ["DISPLAY"] = display

    xvfb_command = [
        "Xvfb",
        display,
        "-screen",
        "0",
        f"{window_width}x{window_height}x24",
    ]
    x11vnc_command = [
        "x11vnc",
        "-display",
        display,
        "-rfbport",
        "5900",
        "-forever",
        "-nopw",
        "-bg",
    ]

    try:
        xvfb = subprocess.Popen(xvfb_command, stderr=subprocess.STDOUT)
        x11vnc = subprocess.Popen(x11vnc_command, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error starting subprocess: {e}")
        sys.exit(1)

    logging.info(
        f"VNC server started on display {display} with resolution {window_width}x{window_height}."
    )

    @atexit.register
    def cleanup():
        logging.info("Terminating VNC server and Xvfb...")
        xvfb.terminate()
        x11vnc.kill()
        xvfb.wait()
        x11vnc.wait()
        logging.info("Cleanup complete.")
        sys.exit(0)


def signal_handler(sig, frame):
    logging.info(f"Received signal {sig}. Cleaning up...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
