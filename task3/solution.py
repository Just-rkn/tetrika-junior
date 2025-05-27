def appearance(intervals: dict[str, list[int]]) -> int:
    def merge_intervals(
            times: list[int], lesson_start: int, lesson_end: int
    ) -> list[list[int]]:
        intervals = [
            [max(times[i], lesson_start), min(times[i + 1], lesson_end)]
            for i in range(0, len(times), 2)
            if times[i] < lesson_end and times[i + 1] > lesson_start
        ]

        intervals = sorted(intervals)

        merged_intervals = []
        for start, end in intervals:
            if not merged_intervals or merged_intervals[-1][1] < start:
                merged_intervals.append([start, end])
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
        return merged_intervals

    def count_common_time(
            first_times: list[list[int]], second_times: list[list[int]]
    ) -> int:
        first_idx = second_idx = total = 0

        while first_idx < len(first_times) and second_idx < len(second_times):
            start = max(first_times[first_idx][0], second_times[second_idx][0])
            end = min(first_times[first_idx][1], second_times[second_idx][1])
            if start < end:
                total += end - start
            if first_times[first_idx][1] < second_times[second_idx][1]:
                first_idx += 1
            else:
                second_idx += 1
        return total

    lesson_start, lesson_end = intervals['lesson']
    pupil_times = merge_intervals(intervals['pupil'], lesson_start, lesson_end)
    tutor_times = merge_intervals(intervals['tutor'], lesson_start, lesson_end)

    return count_common_time(pupil_times, tutor_times)
