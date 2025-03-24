class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        non_meeting = 0
        last_meeting = 0
        meetings.sort()

        for start, end in meetings:
            if start > last_meeting+1:
                non_meeting += (start-last_meeting-1)
            last_meeting = max(last_meeting, end)
            
        non_meeting += days-last_meeting

        return non_meeting
