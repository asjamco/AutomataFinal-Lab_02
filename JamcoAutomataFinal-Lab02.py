class FSMachine:
    def __init__(self):
        pass

    def run_mealy(self, binary_input):
        state = 0
        state_history = [state]
        output_seq = ""

        for bit in binary_input:
            if bit not in {"0", "1"}:
                print("Invalid character found. Please enter only 0 or 1.")
                return

            match state:
                case 0:
                    if bit == "0":
                        state = 1
                        output_seq += "b"
                    else:
                        state = 0
                        output_seq += "b"

                case 1:
                    if bit == "0":
                        output_seq += "b"
                    else:
                        state = 2
                        output_seq += "a"

                case 2:
                    if bit == "0":
                        state = 1
                        output_seq += "b"
                    else:
                        state = 0
                        output_seq += "b"

            state_history.append(state)

        print(f"States Traversed: {' -> '.join(map(str, state_history))}")
        print(f"Output Produced: {output_seq}")

    def run_moore(self, binary_input):
        state = 0
        path = [state]
        outputs = "b"  # initial output

        for bit in binary_input:
            if bit not in {"0", "1"}:
                print("Invalid character found. Please enter only 0 or 1.")
                return

            if state == 0:
                state = 1 if bit == "0" else 0
            elif state == 1:
                state = 1 if bit == "0" else 2
            else:
                state = 1 if bit == "0" else 0

            path.append(state)
            outputs += "b"

        print(f"States Traversed: {' -> '.join(map(str, path))}")
        print(f"Output Produced: {outputs}")


if __name__ == "__main__":
    machine = FSMachine()
    inp1 = input("Input for Mealy FSM: ")
    machine.run_mealy(inp1)
    inp2 = input("Input for Moore FSM: ")
    machine.run_moore(inp2)
