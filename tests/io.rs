use osu_syncflow::file;
use osu_syncflow::parser;

const HEADERS: &[&str] = &["General", "Editor", "Metadata", "Difficulty", "Events", "TimingPoints", "Colours", "HitObjects"];

#[test]
fn test_parsing_headers_real_file() {
    let raw_data = file::read_raw_osu_data("assets/reanimate/reanimate.osu").unwrap();
    let parsed_data = parser::parse_raw_osu_data(&raw_data);

    for header in HEADERS {
        assert!(parsed_data.contains_key(&header.to_string()));
    }
}

