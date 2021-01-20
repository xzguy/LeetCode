class Solution:
    def videoStitching(self, clips: [[int]], T: int) -> int:
        res = 0
        clip_start = 0
        clip_end = 0
        while clip_end < T:
            for clip in clips:
                if clip[0] <= clip_start and clip[1] > clip_end:
                    clip_end = clip[1]
            if clip_start == clip_end:
                return -1
            clip_start = clip_end
            res += 1
        return res