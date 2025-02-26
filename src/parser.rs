use std::collections::HashMap;

pub fn parse_raw_osu_data(raw_file: &str) -> HashMap<String, Vec<String>> {
    let mut osu_beatmap_data: HashMap<String, Vec<String>> = HashMap::new();
    let mut current_section: Option<String> = None;

    for line in raw_file.lines() {
        if line.starts_with('[') && line.ends_with(']') {
            let new_section = line.trim_matches(&['[', ']']);
            current_section = Some(new_section.to_string());
        } else if let Some(ref header) = current_section {
            let data = line.to_string();
            osu_beatmap_data.entry(header.clone()).or_insert_with(Vec::new).push(data);
        }
    }

    osu_beatmap_data
}


#[cfg(test)]
mod tests {
    use super::*;

    const HEADERS: &[&str] = &["General", "Editor", "Metadata", "Difficulty", "Events", "TimingPoints", "Colours", "HitObjects"];

    fn mock_raw_osu_data_simple() -> String {
        HEADERS
            .iter()
            .map(|header| format!("[{}]\nkey: value", header))
            .collect::<Vec<String>>()
            .join("\n\n")
    }

    #[test]
    fn test_parse_raw_osu_data_with_headers() {
        let raw_file_with_headers = mock_raw_osu_data_simple();
        let parsed_osu_file_with_headers = parse_raw_osu_data(&raw_file_with_headers);

        for header in HEADERS {
            assert!(parsed_osu_file_with_headers.contains_key(&header.to_string()));
        }
    }

    #[test]
    fn test_parse_raw_osu_data_fields() {
        let raw_file_with_headers = mock_raw_osu_data_simple();
        let parsed_osu_file_with_headers = parse_raw_osu_data(&raw_file_with_headers);

        for header in HEADERS {
            assert!(parsed_osu_file_with_headers.get(&header.to_string()).unwrap().len() > 0);
        }
    }
}

