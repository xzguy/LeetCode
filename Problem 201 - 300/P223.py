class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        rect_1 = (C-A) * (D-B)
        rect_2 = (G-E) * (H-F)
        if E > C or A > G or B > H or D < F:
            return rect_1 + rect_2
        overlap_left_bottom_x = max(A, E)
        overlap_left_bottom_y = max(B, F)
        overlap_right_top_x = min(G, C)
        overlap_right_top_y = min(H, D)
        overlap_area = (overlap_right_top_x - overlap_left_bottom_x) * (overlap_right_top_y - overlap_left_bottom_y)
        return rect_1 + rect_2 - overlap_area