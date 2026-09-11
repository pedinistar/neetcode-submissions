class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length) return false

        const s_map = new Map()

        for (let char of s) {
            s_map.set(char, (s_map.get(char)||0)+1)
        }

        for (let char of t){
            if(s_map.has(char) && s_map.get(char) > 0){
                s_map.set(char, s_map.get(char)-1)
            } else{
                return false
            }
        }

        return true
    }
}
