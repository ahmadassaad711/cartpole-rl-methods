"""Convenience launcher for the CartPole demos."""

from __future__ import annotations

import argparse


def run_pygame(args: argparse.Namespace) -> None:
    from train_pygame import train_with_visualization

    train_with_visualization(
        num_episodes=args.episodes,
        max_steps_per_episode=args.max_steps,
        render_delay=args.delay,
    )


def run_web(args: argparse.Namespace) -> None:
    import uvicorn

    uvicorn.run(
        "train_web:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Launch CartPole RL demos.")
    parser.add_argument(
        "mode",
        nargs="?",
        default="pygame",
        choices=("pygame", "web"),
        help="Demo mode to run.",
    )
    parser.add_argument("--episodes", type=int, default=500, help="Episodes for the Pygame demo.")
    parser.add_argument("--max-steps", type=int, default=500, help="Maximum steps per episode.")
    parser.add_argument("--delay", type=int, default=0, help="Pygame render delay in milliseconds.")
    parser.add_argument("--host", default="127.0.0.1", help="Web server host.")
    parser.add_argument("--port", type=int, default=8000, help="Web server port.")
    parser.add_argument("--reload", action="store_true", help="Enable uvicorn reload for development.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.mode == "web":
        run_web(args)
    else:
        run_pygame(args)


if __name__ == "__main__":
    main()
