class Solution:
    # recursive way
    def diffWaysToCompute(self, input: str) -> [int]:
        num, s_idx = self.get_next_number(input, 0)
        num_list = [num]
        operator_list = []
        while s_idx < len(input):
            operator = input[s_idx]
            operator_list.append(operator)
            s_idx += 1
            num, s_idx = self.get_next_number(input, s_idx)
            num_list.append(num)
        
        # dp memo
        def sub(ope_lst_start: int, ope_lst_end: int, memo: dict) -> [int]:
            if ope_lst_end == ope_lst_start:
                return [num_list[ope_lst_start]]
            if (ope_lst_start, ope_lst_end) not in memo:
                i = ope_lst_start
                res = []
                while i < ope_lst_end:
                    left_lst = sub(ope_lst_start, i, memo)
                    right_lst = sub(i+1, ope_lst_end, memo)
                    for l in left_lst:
                        for r in right_lst:
                            if operator_list[i] == "+":
                                res.append(l+r)
                            elif operator_list[i] == "-":
                                res.append(l-r)
                            elif operator_list[i] == "*":
                                res.append(l*r)
                    i += 1
                memo[ope_lst_start, ope_lst_end] = res
            return memo[ope_lst_start, ope_lst_end]

        return sub(0, len(operator_list), {})


    def get_next_number(self, input: str, start_idx: int) -> []:
        i = start_idx
        while i < len(input) and input[i] in "0123456789":
            i += 1
        return [int(input[start_idx: i]), i]