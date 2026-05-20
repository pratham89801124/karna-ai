"""
KARNA AI - Entertainment Assistant
Integrates joke generation with voice commands
"""

import logging
from typing import Optional, List, Dict
from entertainment.joke_generator import JokeGenerator, JokeNinjaGenerator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EntertainmentAssistant:
    """Entertainment Assistant for KARNA AI"""
    
    # Voice command mappings
    VOICE_COMMANDS_JOKES = {
        "tell me a joke": "random",
        "tell a joke": "random",
        "make me laugh": "random",
        "joke": "random",
        "random joke": "random",
        
        "programming joke": "programming",
        "programmer joke": "programming",
        "coder joke": "programming",
        "developer joke": "programming",
        "coding joke": "programming",
        "tech joke": "programming",
        
        "knock knock joke": "knock-knock",
        "knock-knock joke": "knock-knock",
        "knock knock": "knock-knock",
        
        "joke of the day": "daily",
        "daily joke": "daily",
        "what's the joke": "daily",
        "todays joke": "daily",
    }
    
    def __init__(self, text_to_speech=None, use_ninja_api: bool = False, api_key: Optional[str] = None):
        """
        Initialize Entertainment Assistant
        
        Args:
            text_to_speech: TextToSpeech instance for speaking jokes
            use_ninja_api: Use Joke Ninja API instead of Official Joke API
            api_key: API key for Joke Ninja (if applicable)
        """
        self.tts = text_to_speech
        self.use_ninja_api = use_ninja_api
        
        if use_ninja_api:
            self.joke_generator = JokeNinjaGenerator(api_key=api_key)
            logger.info("🤖 Using Joke Ninja API")
        else:
            self.joke_generator = JokeGenerator()
            logger.info("🤖 Using Official Joke API")
    
    def process_voice_command(self, command: str) -> bool:
        """
        Process voice command for jokes
        
        Args:
            command: Voice command text
        
        Returns: True if command was processed, False otherwise
        """
        command_lower = command.lower().strip()
        
        # Check if command matches any joke command
        for phrase, joke_type in self.VOICE_COMMANDS_JOKES.items():
            if phrase in command_lower:
                self.tell_joke(joke_type)
                return True
        
        return False
    
    def tell_joke(self, joke_type: str = "random") -> bool:
        """
        Tell a joke and speak it if TTS is available
        
        Args:
            joke_type: Type of joke (random, programming, knock-knock, daily)
        
        Returns: True if joke was told successfully
        """
        logger.info(f"🎭 Fetching {joke_type} joke...")
        
        joke = None
        
        # Fetch joke based on type
        if joke_type == "random":
            joke = self.joke_generator.get_random_joke()
        elif joke_type == "programming":
            joke = self.joke_generator.get_programming_joke()
        elif joke_type == "knock-knock":
            joke = self.joke_generator.get_knock_knock_joke()
        elif joke_type == "daily":
            joke = self.joke_generator.get_joke_of_the_day()
        
        if not joke:
            error_msg = f"❌ Could not fetch {joke_type} joke at this moment."
            logger.error(error_msg)
            if self.tts:
                self.tts.speak(error_msg)
            return False
        
        # Format joke
        formatted_joke = JokeGenerator.format_joke(joke)
        print(formatted_joke)
        
        # Speak joke if TTS available
        if self.tts:
            # Extract and speak setup and punchline
            setup = joke.get("setup", "")
            punchline = joke.get("punchline", "")
            
            if setup and punchline:
                self.tts.speak(setup)
                self.tts.speak(punchline)
                logger.info("✅ Joke spoken")
        
        return True
    
    def get_multiple_jokes(self, count: int = 5, joke_type: str = "general") -> Optional[List[str]]:
        """
        Get multiple jokes
        
        Args:
            count: Number of jokes to get
            joke_type: Type of jokes
        
        Returns: List of formatted jokes
        """
        logger.info(f"🎭 Fetching {count} {joke_type} jokes...")
        
        jokes = self.joke_generator.get_jokes_by_type(joke_type, count=count)
        
        if not jokes:
            logger.error(f"❌ Failed to fetch {count} jokes")
            return None
        
        formatted_jokes = []
        for joke in jokes:
            formatted = JokeGenerator.format_joke(joke)
            formatted_jokes.append(formatted)
        
        return formatted_jokes
    
    def get_joke_and_text(self, joke_type: str = "random") -> tuple:
        """
        Get a joke and return both formatted text and spoken text
        
        Args:
            joke_type: Type of joke
        
        Returns: Tuple of (formatted_text, spoken_text)
        """
        if joke_type == "random":
            joke = self.joke_generator.get_random_joke()
        elif joke_type == "programming":
            joke = self.joke_generator.get_programming_joke()
        elif joke_type == "knock-knock":
            joke = self.joke_generator.get_knock_knock_joke()
        elif joke_type == "daily":
            joke = self.joke_generator.get_joke_of_the_day()
        else:
            joke = None
        
        if not joke:
            return ("❌ Joke not available", "Failed to fetch joke")
        
        formatted_text = JokeGenerator.format_joke(joke)
        
        setup = joke.get("setup", "")
        punchline = joke.get("punchline", "")
        spoken_text = f"{setup}. {punchline}"
        
        return (formatted_text, spoken_text)
    
    def close(self):
        """Close resources"""
        if hasattr(self.joke_generator, 'close'):
            self.joke_generator.close()
        logger.info("🔌 Entertainment assistant closed")


def demo():
    """Demo the Entertainment Assistant"""
    print("\n" + "="*60)
    print("🎭 KARNA AI - Entertainment Assistant Demo")
    print("="*60 + "\n")
    
    # Note: TTS not included in this demo for simplicity
    assistant = EntertainmentAssistant(text_to_speech=None)
    
    # Simulate voice commands
    voice_commands = [
        "Tell me a joke",
        "Programming joke",
        "Tell a knock knock joke",
        "What's the joke of the day",
    ]
    
    for command in voice_commands:
        print(f"\n🎤 Voice Command: '{command}'")
        print("-" * 40)
        assistant.process_voice_command(command)
    
    # Get multiple jokes
    print("\n" + "="*60)
    print("Multiple Jokes Example:")
    print("="*60)
    jokes = assistant.get_multiple_jokes(count=3, joke_type="general")
    if jokes:
        for i, joke in enumerate(jokes, 1):
            print(f"\nJoke {i}:")
            print(joke)
    
    assistant.close()
    print("\n" + "="*60)
    print("✅ Demo Complete!")
    print("="*60 + "\n")


if __name__ == "__main__":
    demo()
