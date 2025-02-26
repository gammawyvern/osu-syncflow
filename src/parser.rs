use std::collections::HashMap;

pub fn parse_raw_osu_data(raw_file: &str) -> HashMap<String, Vec<String>> {
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

    const HEADERS: &[&str] = &["General", "Editor", "Metadata", "Difficulty", "Events", "TimingPoints", "Colours", "HitObjects"];

    #[test]
    fn test_parse_raw_osu_data_with_headers() {
        let raw_file_with_headers = HEADERS
            .iter()
            .map(|header| format!("[{}]\nkey: value", header))
            .collect::<Vec<String>>()
            .join("\n\n");

        let parsed_osu_file_with_headers = parse_raw_osu_data(&raw_file_with_headers);

        for header in HEADERS {
            assert!(parsed_osu_file_with_headers.contains_key(&header.to_string()));
        }
    }
}
