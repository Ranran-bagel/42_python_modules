# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_stream.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/19 15:49:53 by wezhou            #+#    #+#              #
#    Updated: 2026/06/19 18:11:43 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "sleep", "grab",
                 "move", "swim", "eat",
                 "climb", "release"]
    while True:
        yield (random.choice(players), random.choice(actions))

def consume_event(event_lst: list) -> typing.Generator[tuple[str, str], None, None]:
    while event_lst:
        index = random.randint(0, len(event_lst) - 1)
        event = event_lst[index]
        del event_lst[index]
        yield event

def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()
    for i in range(0, 1000):
        event = next(event_gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    event_lst = []
    for i in range(0, 10):
        event = next(event_gen)
        event_lst.append(event)
    print(f"Built list of 10 events: {event_lst}")
    for event in consume_event(event_lst):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_lst}")


if __name__ == "__main__":
    main()
