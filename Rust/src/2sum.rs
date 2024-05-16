use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut checker = HashMap::new();


        for (key,&val) in nums.iter().enumerate() {
            let tmp = target - val;
            match checker.get(&tmp) {
                Some(&ans) => return vec![ans as i32, key as i32],
                None => { checker.insert(val, key); },
            }
        }
        vec![] // return an empty vector if no solution is found
    }
}