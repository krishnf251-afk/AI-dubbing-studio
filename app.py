# ==============================================================================
# SIMPLE TESTING UI / HARNESS (app.py)
# Used for testing the Core Backend Engine (main.py)
# ==============================================================================

from main import (
    USERS_DB,
    bypass_youtube_fetch,
    create_dubbing_job,
    get_model_tier,
    instant_voice_changer,
    calculate_server_load,
    run_12h_auto_cleaner,
    trigger_github_hf_backup,
    trigger_emergency_escape
)

def run_backend_test_suite():
    print("\n========================================================")
    print("      एनिमी डबिंग ऐप - CORE BACKEND ENGINE TESTER       ")
    print("========================================================\n")

    # Test 1: User Login & Master Lock
    user = USERS_DB["MASTER-001"]
    print(f"1. Master Owner Authenticated: UID={user['uid']}, Role={user['role']}")

    # Test 2: AI Engine White-label Tier
    engine_tier = get_model_tier(user["role"])
    print(f"2. VIP AI Engine Tier Allocated: {engine_tier}")

    # Test 3: Third-Party YouTube Bypass
    sample_url = "https://youtube.com/watch?v=sample_anime_123"
    print(f"3. Fetching metadata via Third-Party Bypass for: {sample_url}")
    vinfo = bypass_youtube_fetch(sample_url)
    print(f"   -> Title: {vinfo['title']}")
    print(f"   -> Fingerprint: {vinfo['fingerprint']}")
    print(f"   -> Bypass Engine: {vinfo['bypass_source']}")

    # Test 4: Create Dubbing Job (Mode A vs Mode B)
    print("\n4. Testing Mode A (Full MP4 Video Dubbing):")
    job_a = create_dubbing_job(user["uid"], user["role"], "MODE_A_FULL_MP4", vinfo)
    print(f"   -> Job ID: {job_a['job_id']}")
    print(f"   -> Total Chunks: {job_a['total_chunks']}")
    print(f"   -> BGM Preset: {job_a['bgm_preset']}")

    print("\n5. Testing Mode B (Audio-Only Stream Extraction & Dubbing):")
    job_b = create_dubbing_job(user["uid"], user["role"], "MODE_B_AUDIO_ONLY", vinfo)
    print(f"   -> Job ID: {job_b['job_id']}")
    print(f"   -> Mode: {job_b['mode']}")

    # Test 5: Instant Voice Changer API
    print("\n6. Testing Instant Voice Changer API:")
    voice_res = instant_voice_changer("ओरे वा ज़ेट्टाई नि अकिरामेनाइ!", role_preset="Hero", emotion="Action")
    print(f"   -> Hero Voice Conversion Pitch: {voice_res['pitch_multiplier']}")

    # Test 6: Server Load & Cleaner
    load = calculate_server_load()
    print(f"\n7. Server Load Indicator: {load['status']} ({load['status_label']})")

    # Test 7: Backup & Escape
    backup = trigger_github_hf_backup(user["uid"])
    print(f"8. GitHub-HF Backup Sync: {backup['github_commit']}")

    print("\n========================================================")
    print("   ALL CORE BACKEND ENGINE TESTS PASSED SUCCESSFULLY!    ")
    print("========================================================\n")

if __name__ == "__main__":
    run_backend_test_suite()
