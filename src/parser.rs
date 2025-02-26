use std::collections::HashMap;

pub fn parse_raw_osu_file(raw_file: &str) -> HashMap<String, Vec<String>> {
    let mut osu_beatmap_data: HashMap<String, Vec<String>> = HashMap::new();

    for line in raw_file.lines() {
        if line.starts_with('[') && line.ends_with(']') {
            let section_name = line.trim_start_matches('[').trim_end_matches(']').to_string();
            osu_beatmap_data.entry(section_name).or_insert_with(Vec::new);
        }
    }

    osu_beatmap_data
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_raw_osu_file_has_general() {
        let raw_file_with_general = "[General]\nSome: data";
        let parsed_osu_file_with_general = parse_raw_osu_file(raw_file_with_general);

        assert!(parsed_osu_file_with_general.contains_key("General"));
    }
}
