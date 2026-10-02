# 🧠 Bass Guitar Instructor — Custom AI Skill

## 📌 Project Overview

This project demonstrates the design of a custom AI skill that transforms
an AI assistant into a structured bass-guitar instructor and practice coach.

Rather than relying on a single prompt, the skill defines how the AI should
receive user information, select an appropriate instructional approach,
follow a teaching workflow, make decisions based on player needs, structure
its responses, and validate the quality of its output.

---

## 🎯 Project Objective

The objective was to design a reusable AI instruction system capable of
providing bass-guitar guidance that adapts to different players and
learning situations.

The skill considers factors such as:

- Player skill level
- Bass type
- Number of strings
- Musical genre
- Technique or topic
- Practice goals
- Available practice time
- Gear context
- Desired output format

---

## 🧩 Skill Architecture

The AI skill follows a seven-part architecture:

### 1. Trigger

Defines when the skill should activate and the types of bass-related
requests it is designed to handle.

### 2. Input

Identifies the information needed to personalize the response to the
individual player and learning situation.

### 3. Sources

Establishes the reference materials and knowledge hierarchy the AI
should use when generating instruction.

### 4. Workflow

Defines the step-by-step process the AI follows when responding to
a bass-related request.

### 5. Decision Rules

Adjusts the response according to factors such as player level,
musical context, learning goals, and practice needs.

### 6. Output

Defines how the final instructional response should be structured
and presented to the user.

### 7. Validation

Provides a quality-control checklist used to evaluate the response
before it is delivered.

---

## 🔄 AI Workflow

The skill follows a structured instructional process:

**Understand the Player → Clarify the Goal → Diagnose the Need →
Explain the Concept → Demonstrate → Create a Practice Plan →
Identify Common Mistakes → Recommend Next Steps → Validate Output**

This workflow helps ensure that the AI does more than simply answer
a question. It provides structured, practical, and actionable instruction.

---

## 🎚️ Adaptive Decision Logic

The skill changes its instructional approach according to the player's
experience level.

### 🌱 Beginner

Prioritizes:

- Simple explanations
- Fundamental technique
- Timing and rhythm
- Basic fretboard knowledge
- Manageable practice exercises
- Clear step-by-step instructions

### 🎸 Intermediate

Introduces:

- Deeper fretboard knowledge
- Groove development
- Harmonic understanding
- Technique refinement
- Stylistic application
- More structured practice routines

### 🎵 Advanced / Professional

Focuses on:

- Advanced musicianship
- Articulation
- Stylistic nuance
- Harmonic choices
- Improvisation
- Tone development
- Performance context

---

## 🛠️ Skills Demonstrated

`AI Instruction Design` `Prompt Engineering` `Workflow Design`

`Decision Logic` `Context-Aware AI` `AI Behavior Design`

`Output Structuring` `Validation` `AI Quality Control`

---

## 💡 Why This Project Matters

Effective AI systems require more than simply writing a question and
accepting the generated response.

This project demonstrates how structured instructions, contextual inputs,
decision rules, workflow design, output requirements, and validation
criteria can be used to create more consistent and useful AI behavior.

The project also demonstrates the transition from individual prompting
toward designing a reusable AI instruction system.

---

## 📄 Skill Implementation

The complete implementation of the AI skill is available in:

**[`SKILL.md`](SKILL.md)**

The skill file contains the detailed instructions governing:

- When the skill activates
- Information it should collect
- Sources it should prioritize
- Teaching workflow
- Decision rules
- Response structure
- Validation requirements

---

## 🧪 Example Use Cases

The AI skill can support requests such as:

- Creating a beginner bass practice routine
- Explaining scales and arpeggios
- Improving timing and groove
- Learning gospel, jazz, funk, and other styles
- Understanding fretboard relationships
- Developing bass technique
- Troubleshooting bass tone
- Creating structured practice plans
- Improving improvisation
- Understanding how to approach songs

---

## 📊 Example Interaction

### User Request

> I am an intermediate 5-string bass player interested in gospel music.
> I have 30 minutes per day to practice and want to improve my timing,
> fretboard knowledge, and ability to create fills.

### AI Skill Process

The skill evaluates:

**Player Level → Instrument → Genre → Goals → Available Time →
Instructional Approach → Practice Structure → Validation**

The resulting response should provide instruction appropriate to the
player's experience, musical context, goals, and available practice time.

---

## ✅ Validation Approach

Before producing the final response, the skill checks whether the
instruction is:

- Appropriate for the player's level
- Relevant to the stated goal
- Clear and understandable
- Musically practical
- Actionable during practice
- Structured appropriately
- Consistent with the requested format

This validation layer is intended to improve the consistency and
usefulness of AI-generated instruction.

---

## 📚 Key Takeaways

This project strengthened my understanding of designing reusable AI
instructions rather than relying solely on individual prompts.

It demonstrates how AI behavior can be shaped through:

- Structured workflows
- Contextual inputs
- Decision rules
- Adaptive responses
- Output requirements
- Validation criteria

The project also reinforced the importance of designing AI systems around
the user's context and intended outcome rather than treating every request
the same way.
