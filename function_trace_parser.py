def main(file_path):
    # unique event count
    event_set = set()
    # carry each event info
    list_of_events = []
    # create connection between parent -> child
    parent_to_children = {}

    parent_name_to_child_name = {}

    event_name_list = set()
    with open(file_path) as file:
        for i in range(11):
            next(file)

        for line in file:
            line = line.strip()
            line = line.split(",")
            # parent and child
            if len(line) == 6:
                parent = line[0]
                parent_description = line[1]
                child = line[2]
                child_description = line[3]
                child_scheduled_at = line[4]
                child_will_execute_at = line[5]

                event_set.add(parent)
                event_set.add(child)
                list_of_events.append(
                    (
                        parent,
                        parent_description,
                        child,
                        child_description,
                        child_scheduled_at,
                        child_will_execute_at,
                    )
                )
                if parent not in parent_to_children:
                    parent_to_children[parent] = set()
                parent_to_children[parent].add(child)

                # attempt to get more specific event names
                parent_description = parent_description.replace(
                    ".wrapped_function_event", ""
                )
                child_description = child_description.replace(
                    ".wrapped_function_event", ""
                )
                event_name_list.add(parent_description)
                event_name_list.add(child_description)
                if parent_description not in parent_name_to_child_name:
                    parent_name_to_child_name[parent_description] = set()
                parent_name_to_child_name[parent_description].add(
                    child_description
                )

            # no parent event (initial schedule)
            elif len(line) == 4:
                parent = line[0]
                parent_description = line[1]
                scheduled_at = line[2]
                will_execute_at = line[3]
                list_of_events.append(
                    (
                        parent,
                        parent_description,
                        None,
                        None,
                        scheduled_at,
                        will_execute_at,
                    )
                )
                if parent not in parent_to_children:
                    parent_to_children[parent] = set()
                event_set.add(parent)

                # attempt to get more specific event names
                parent_description = parent_description.replace(
                    ".wrapped_function_event", ""
                )
                event_name_list.add(parent_description)
                if parent_description not in parent_name_to_child_name:
                    parent_name_to_child_name[parent_description] = set()

            # in case of bad line
            else:
                continue

    # def print_call_graph(parent_to_children):
    # 	"""
    # 	prints call graph using addresses
    # 	ex: 0x570aafcd3290 -> 0x570aafcd3218, 0x570aafcd3290, 0x570aafcd3308
    # 	"""
    # 	for parent, children in parent_to_children.items():
    # 		print(f"{parent} -> {', '.join(children)}")

    def print_name_call_graph(parent_name_to_child_name):
        for parent, child in parent_name_to_child_name.items():
            print(f"{parent} -> {', '.join(child)}")

    print(print_name_call_graph(parent_name_to_child_name))

    for i in range(len(event_name_list)):
        print(f"{i}: {list(event_name_list)[i]}")


if __name__ == "__main__":
    file = input(
        "Select 1 O3 CPU trace, 2 for TIMING trace, 3 for ATOMIC trace:"
    )
    if file == "1":
        main("cpu_traces/O3_trace.txt")
    elif file == "2":
        main("cpu_traces/TIMING_trace.txt")
    elif file == "3":
        main("cpu_traces/ATOMIC_trace.txt")
