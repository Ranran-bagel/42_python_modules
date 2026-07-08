import sys


def main() -> None:
    score_lst: list[int] = []
    print("=== Player Score Analytics ===")
    for arg in sys.argv[1:]:
        try:
            score_lst.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if len(score_lst) == 0:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {score_lst}")
        print(f"Total players: {len(score_lst)}")
        print(f"Total score: {sum(score_lst)}")
        print(f"Average score: {sum(score_lst) / len(score_lst)}")
        print(f"High score: {max(score_lst)}")
        print(f"Low score: {min(score_lst)}")
        print(f"Score range: {max(score_lst) - min(score_lst)}")


if __name__ == "__main__":
    main()
