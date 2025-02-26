use std::fs;

pub fn read_raw_osu_data(path: &str) -> Result<String, std::io::Error> {
    fs::read_to_string(path)
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_read_raw_osu_data_success() {
        let content = read_raw_osu_data("assets/reanimate/reanimate.osu").expect("Failed to read file.");
        assert!(content.contains("[HitObjects]"));
    }

    #[test]
    fn test_read_raw_osu_data_failure() {
        let not_found = read_raw_osu_data("assets/dne.osu");
        assert!(not_found.is_err());
    }

    #[test]
    fn test_read_raw_osu_data_empty_path() {
        let not_found = read_raw_osu_data("");
        assert!(not_found.is_err());
    }
}

