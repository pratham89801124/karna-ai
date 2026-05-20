"""
KARNA AI - Joke Generator Usage Guide
======================================

This guide shows you how to use the new Joke Generator feature in KARNA AI.
"""

# ============================================================================
# BASIC USAGE - Standalone Joke Generator
# ============================================================================

from entertainment.joke_generator import JokeGenerator

# Create instance
joke_gen = JokeGenerator()

# Get a random joke
joke = joke_gen.get_random_joke()
print(joke_gen.format_joke(joke))

# Get a programming joke
prog_joke = joke_gen.get_programming_joke()
print(joke_gen.format_joke(prog_joke))

# Get a knock-knock joke
kk_joke = joke_gen.get_knock_knock_joke()
print(joke_gen.format_joke(kk_joke))

# Get joke of the day
jotd = joke_gen.get_joke_of_the_day()
print(joke_gen.format_joke(jotd))

# Get multiple jokes by type
jokes = joke_gen.get_jokes_by_type("general")
for joke in jokes:
    print(joke_gen.format_joke(joke))


# ============================================================================
# VOICE COMMAND INTEGRATION - Use with KARNA AI
# ============================================================================

from entertainment.entertainment_assistant import EntertainmentAssistant
from voice.text_to_speech import TextToSpeech

# Create instances
tts = TextToSpeech()
entertainment = EntertainmentAssistant(text_to_speech=tts)

# Tell a random joke (will be spoken)
entertainment.tell_joke("random")

# Tell a programming joke (will be spoken)
entertainment.tell_joke("programming")

# Tell a knock-knock joke (will be spoken)
entertainment.tell_joke("knock-knock")

# Get multiple jokes
multiple_jokes = entertainment.get_multiple_jokes(count=5)
for joke in multiple_jokes:
    print(joke)


# ============================================================================
# AVAILABLE VOICE COMMANDS IN KARNA AI
# ============================================================================

"""
When running main.py, you can use these voice commands:

1. "Tell me a joke"
   - Gets and speaks a random joke

2. "Tell a programming joke"
   - Gets and speaks a programming-related joke

3. "Tell a knock knock joke"
   - Gets and speaks a knock-knock joke

4. "What's the joke of the day"
   - Gets and speaks today's featured joke

5. "Make me laugh"
   - Gets and speaks a random joke

Just say "Hey Karna" to activate voice listening, then use any of these commands!
"""


# ============================================================================
# API INFORMATION
# ============================================================================

"""
🌐 Official Joke API
URL: https://official-joke-api.appspot.com

Features:
- No API key required
- Free tier: Unlimited requests
- Endpoints:
  * /random_joke - Single random joke
  * /jokes/{type}/random - Random joke by type
  * /jokes/{type}/ten - 10 jokes by type
  * /jod - Joke of the day

Types:
- general
- programming
- knock-knock

Response Format:
{
  "type": "general",
  "setup": "Why did the chicken cross the road?",
  "punchline": "To get to the other side!",
  "id": 1
}

🌐 Alternative: Joke Ninja API
URL: https://api-ninjas.com/api/jokes

Features:
- Free tier available (up to 10,000 requests/month)
- Optional API key for higher limits
- Supports categories
"""


# ============================================================================
# ERROR HANDLING
# ============================================================================

"""
The joke generator includes error handling for:
- Network timeouts
- Connection errors
- HTTP errors
- JSON parsing errors

All errors are logged and handled gracefully.
If API is unavailable, the assistant will inform the user.
"""


# ============================================================================
# RUNNING THE DEMO
# ============================================================================

"""
To test the joke generator:

1. Run the standalone demo:
   python entertainment/joke_generator.py

2. Run the entertainment module demo:
   python entertainment/entertainment_assistant.py

3. Run full KARNA AI with voice commands:
   python main.py
   Then say: "Hey Karna, tell me a joke"
"""

# ============================================================================
# CUSTOMIZATION
# ============================================================================

"""
To add more joke APIs or customize:

1. Edit entertainment/joke_generator.py to add new API classes
2. Edit VOICE_COMMANDS_JOKES dict in entertainment/entertainment_assistant.py
3. Add new commands to process_voice_command() in main.py

Example: Adding a new API

class CustomJokeAPI:
    BASE_URL = "https://your-api.com"
    
    def get_random_joke(self):
        # Implementation
        pass

Then integrate it into EntertainmentAssistant class.
"""
