class MachineAssignment:

    def mealy_machine(self, sequence):
        current_state = 0
        path = [current_state]
        result = []

        for bit in sequence:
            if bit not in ('0', '1'):
                print("Invalid input detected.")
                return

            if current_state == 0:
                if bit == '0':
                    current_state = 1
                    result.append('b')
                else:
                    current_state = 0
                    result.append('b')

            elif current_state == 1:
                if bit == '0':
                    current_state = 1
                    result.append('b')
                else:
                    current_state = 2
                    result.append('a')

            elif current_state == 2:
                if bit == '0':
                    current_state = 1
                    result.append('b')
                else:
                    current_state = 0
                    result.append('b')

            path.append(current_state)

        print("Visited States:", ' -> '.join(map(str, path)))
        print("Output Sequence:", ''.join(result))

    def moore_machine(self, sequence):
        current_state = 0
        path = [current_state]
        output_trace = ['b']  # initial output for state 0

        for bit in sequence:
            if bit not in ('0', '1'):
                print("Invalid input detected.")
                return

            if current_state == 0:
                current_state = 1 if bit == '0' else 0
            elif current_state == 1:
                current_state = 1 if bit == '0' else 2
            elif current_state == 2:
                current_state = 1 if bit == '0' else 0

            path.append(current_state)
            # all states produce 'b' output for now
            output_trace.append('b')

        print("Visited States:", ' -> '.join(map(str, path)))
        print("Output Sequence:", ''.join(output_trace))


if __name__ == "__main__":
    machine = MachineAssignment()
    seq1 = input("Enter binary input for Mealy Machine: ")
    machine.mealy_machine(seq1)
    seq2 = input("Enter binary input for Moore Machine: ")
    machine.moore_machine(seq2)
