use std::collections::HashMap;

fn parse_raw_osu_file(raw_file: &str) -> HashMap<String, String> {
    let mut osu_beatmap_data = HashMap::new();

    for line in raw_file.lines() {
        println!("{}", line);
    }

    return osu_beatmap_data;
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_raw_osu_file_has_general() {
        // let raw_file_with_general = String::from("[General]\nSome: data");
        let raw_file_with_general = "[General]\nSome: data";
        let parsed_osu_file_with_general = parse_raw_osu_file(raw_file_with_general);

        assert!(parsed_osu_file_with_general.contains_key("General"));
    }
}
