class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = [start]
        track = [start]
        while len(track):
            now_idx = track.pop(0)
            if arr[now_idx] == 0:
                return True
            
            for k in [now_idx-arr[now_idx], now_idx+arr[now_idx]]:
                if k in seen:
                    continue
                    
                if 0 <= k < len(arr):
                    track.append(k)
                    seen.append(k)
                    
                
        
        return False
