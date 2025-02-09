import SCStickMap.core
import argparse

def main():
    parser = argparse.ArgumentParser(description="Labeller of Star Citizen keybindings on a PDF")
    parser.add_argument("--key-map-path", "-k", type=str, help="Star Citizen key mapping xml file path.")

    args = parser.parse_args()
    core.SCStickMap(key_map_path=args.key_map_path)


if __name__ == "__main__":
    main()

