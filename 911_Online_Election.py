class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        count_person = {} # 候選人有幾票的字典
        self.lead_list = []  # 每個時間點的領先人的list
        self.times = times
        lead = 0 #領先人
        
        # 建立字典，count_person={0:0, 1:0, 2:0, ...}
        #for p in persons:
        #    count_person[p]=0
        count_person = count_person.fromkeys(persons, 0)
        # 尋找每個時間點的領先人
        for p, t in zip(persons, times):
            count_person[p] += 1 # 現在時間點哪個候選人票數+1
            # 如果現在時間點的候選人票數 > 領先人，則領先人為現在候選人
            if count_person[lead] <= count_person[p]:
                lead = p
            self.lead_list.append(lead) # 依照時間點存入領先人
            
    def q(self, t: int) -> int:
        # 二元搜尋
        left, right = 0, len(self.times) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.times[mid] == t:
                return self.lead_list[mid]
            elif self.times[mid] > t:
                right = mid - 1
            else:
                left = mid + 1
        return self.lead_list[left-1]
