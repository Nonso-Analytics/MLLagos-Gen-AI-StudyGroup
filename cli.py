import argparse
import sys
from app import GeminiCLI

def main():
    parser = argparse.ArgumentParser(
        description="Ask Gemini AI from the terminal",
        epilog="Example: python cli.py 'What is machine learning?'"
    )
    parser.add_argument("question", type=str, help="Question to ask Gemini")
    parser.add_argument("-m", "--model", type=str, default="gemini-2.5-flash",
                       help="Model to use (default: gemini-2.5-flash)")
    
    args = parser.parse_args()
    
    try:
        cli = GeminiCLI(model_name=args.model)
        print(f"\nAsking Gemini: {args.question}\n")
        response = cli.ask(args.question)
        print(response)
        print("\n" + "="*50 + "\n")
    except ValueError as e:
        print(f"Configuration Error: {e}", file=sys.stderr)
        print("\nTip: Create a .env file with GEMINI_API_KEY=your_key", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
