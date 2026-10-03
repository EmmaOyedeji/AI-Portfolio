# Test Case 03 — Advanced Jazz Bass Player

## 🎯 Test Objective

Evaluate whether the Bass Guitar Instructor AI Skill can adapt its
instructional approach for an advanced player and produce appropriately
sophisticated jazz improvisation exercises.

---

## 👤 User Context

| Variable | Value |
|---|---|
| Skill Level | Advanced |
| Instrument | 5-string bass |
| Genre | Jazz |
| Practice Time | 45 minutes per day |
| Existing Knowledge | Scales, modes, chord construction, arpeggios, basic jazz harmony |
| Primary Challenges | Melodic soloing, voice leading, chromaticism, fretboard navigation, rhythmic phrasing |
| Goal | Improve jazz improvisation over ii–V–I progressions and fast chord changes |
| Requested Output | 7-day advanced practice plan |

---

## 📝 Test Prompt

> I'm an advanced bass player using a 5-string bass.
>
> I have strong knowledge of scales, modes, chord construction,
> arpeggios, and basic jazz harmony.
>
> I want to improve my jazz improvisation, especially over ii–V–I
> progressions and chord changes that move quickly.
>
> My biggest challenges are:
> - creating melodic bass solos instead of simply running scales,
> - connecting chord tones smoothly across changes,
> - using chromatic approach notes tastefully,
> - navigating the entire fretboard while improvising, and
> - developing stronger rhythmic phrasing.
>
> I can practice for 45 minutes a day.
>
> Create a 7-day advanced practice plan focused on these areas.
>
> Include specific ii–V–I examples, fretboard exercises, chord-tone
> targeting exercises, chromatic approach-note exercises, rhythmic
> constraints, suggested metronome tempos, and improvisation exercises.

---

## 🤖 Actual Output

| Day | Focus | 10 min | 10 min | 10 min | 15 min |
|---|---|---|---|---|---|
| **1** | Chord-tone voice leading | ii–V–I chord mapping | Guide-tone connections | Restricted improvisation | Full ii–V–I soloing |
| **2** | Melodic development | Motif creation | Motif displacement | Motif through changes | Melodic solos |
| **3** | Chromatic approaches | Single approach notes | Double approaches | Enclosures | Chromatic improvisation |
| **4** | Fretboard freedom | Position mapping | String-set limitation | Position shifts | Full-neck improvisation |
| **5** | Fast changes | 2-beat changes | Target-note drills | Continuous eighth notes | Fast ii–V–I |
| **6** | Rhythmic phrasing | Rhythmic cells | Displacement | Space/rest constraints | Conversational soloing |
| **7** | Integration | Review vocabulary | Full-neck ii–V–I | Chorus constraints | Performance + review |

---

## ✅ Validation Results

| Criterion | Result | Observation |
|---|---|---|
| Appropriate for advanced level | PASS | Uses advanced concepts including guide tones, enclosures, motif development, displacement and voice leading. |
| Respects available practice time | PASS | Each session totals exactly 45 minutes. |
| Addresses melodic improvisation | PASS | Motif development and melodic soloing are directly incorporated. |
| Addresses chord-tone connections | PASS | Voice leading, guide-tone connections and target-note drills are included. |
| Addresses chromaticism | PASS | Single approaches, double approaches and enclosures are included. |
| Addresses fretboard navigation | PASS | Position mapping, string-set limitations, shifts and full-neck improvisation are included. |
| Addresses rhythmic phrasing | PASS | Rhythmic cells, displacement, rests and conversational phrasing are incorporated. |
| Provides improvisation exercises | PASS | Improvisation is incorporated throughout the plan. |
| Provides specific ii–V–I examples | NEEDS IMPROVEMENT | ii–V–I practice is included, but specific chord progressions such as Dm7–G7–Cmaj7 are not provided. |
| Provides requested metronome tempos | NEEDS IMPROVEMENT | No specific BPM targets are included. |
| Uses 5-string-specific possibilities | PARTIAL | Full-neck work is included, but the low B string is not explicitly addressed. |
| Provides detailed execution instructions | PARTIAL | Advanced exercises are named but detailed execution steps are limited. |

---

## 🔍 Issues Identified

The advanced test demonstrated substantial adaptation, but several
areas could be improved:

1. The user explicitly requested specific ii–V–I examples, but the
   response refers to ii–V–I practice without specifying actual chords.

2. Suggested metronome tempos were explicitly requested but were omitted.

3. The user specified a 5-string bass, but the low B string was not
   explicitly incorporated.

4. Some advanced exercises are named without explaining exactly how
   they should be executed.

---

## 🔄 Comparison Across All Three Tests

### Test 01 — Beginner

Focused on:

- Open strings
- Basic fretboard notes
- Quarter and eighth notes
- Simple grooves
- Basic gospel application

### Test 02 — Intermediate

Focused on:

- Chord-to-chord fills
- Position shifting
- Target notes
- Gospel vocabulary
- Drummer interaction
- Musical restraint

### Test 03 — Advanced

Focused on:

- Chord-tone voice leading
- Guide-tone connections
- Motif development
- Chromatic approaches
- Enclosures
- Full-neck improvisation
- Fast chord changes
- Rhythmic displacement
- Conversational soloing

The progression demonstrates that the skill changes the complexity and
instructional focus according to the player's experience and goals.

---

## 💡 Recommended Skill Improvements

Based on this test, future versions of the skill should:

- Verify that every explicitly requested deliverable is included.
- Provide concrete chord examples when harmonic exercises are requested.
- Include BPM targets when metronome tempos are requested.
- Explicitly incorporate extended-range strings for 5- and 6-string players.
- Provide clearer execution instructions for complex exercises.
- Add measurable criteria for determining when an exercise has been mastered.

---

## 📊 Test Conclusion

The skill demonstrated strong adaptation to an advanced player by
shifting away from fundamental instruction and toward sophisticated
improvisational concepts.

The test also revealed an important limitation: although the overall
instructional level adapted successfully, some explicit user requirements
were omitted.

This demonstrates why both adaptive behavior and requirement-compliance
validation are important when evaluating AI-generated instruction.
