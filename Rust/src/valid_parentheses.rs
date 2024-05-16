impl Solution {
    pub fn is_valid(s: String) -> bool {
        
        let mut stack: Vec<char> = Vec::new();
        let opening = std::collections::HashMap::from([(']', '['), (')', '('), ('}', '{')]);

        for c in s.chars() {
           match c {
                '(' => stack.push(c),
                '[' => stack.push(c),
                '{' => stack.push(c),
                _ => {
                    if stack.iter().last() == opening.get(&c) {
                        stack.pop();
                    } else {
                        return false;
                    }
                }
            }
        }

        stack.is_empty()
    }
}