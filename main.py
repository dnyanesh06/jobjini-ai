import random
import requests

def get_user_info():
    """Collects user information (name, qualifications, skills)."""
    print("Hello! I'm your AI-powered Job Recommendation Bot.")
    first_name = input("To start, please tell me your first name: ")
    qualifications = input("What are your qualifications? (e.g., Bachelor's Degree in Computer Science): ")
    skills = input("Enter your skills, separated by commas (e.g., Python, Java, 3D animation): ").split(',')
    skills = [skill.strip().lower() for skill in skills]
    print(f"Thanks, {first_name}! I'm analyzing your qualifications and skills...")
    return first_name, qualifications, skills

def recommend_jobs(skills):
    """Recommends jobs based on skills from a local database."""
    companies_and_jobs = {
        "Google": ["Software Engineer", "AI Researcher", "Data Scientist", "Cloud Engineer", "UX Designer", "Product Manager", "Data Analyst", "Cybersecurity Analyst"],
        "Microsoft": ["Software Engineer", "Cloud Engineer", "AI Researcher", "Data Scientist", "Product Manager", "Technical Writer", "Solutions Architect", "DevOps Engineer"],
        "Amazon": ["Software Engineer", "Data Scientist", "Cloud Engineer", "Product Manager", "Business Analyst", "Marketing Specialist", "Operations Manager", "Warehouse Associate"],
        "Meta": ["Software Engineer", "AI Researcher", "Data Scientist", "Product Designer", "Marketing Specialist", "Content Creator", "Community Manager", "Data Engineer"],
        "Netflix": ["Software Engineer", "Data Scientist", "Machine Learning Engineer", "UX Designer", "Content Creator", "Streaming Engineer", "Security Engineer", "Product Analyst"],
        "Pixar": ["3D Animator", "VFX Artist", "Character Rigger", "Story Artist", "Animation Director", "Lighting Artist", "Compositor", "Render Technical Director"],
        "DreamWorks Animation": ["3D Animator", "VFX Artist", "Character Modeler", "Story Artist", "Animation Director", "Layout Artist", "Storyboard Artist", "FX Artist"],
        "Industrial Light & Magic (ILM)": ["VFX Artist", "3D Modeler", "Compositor", "Lighting Artist", "FX Artist", "Concept Artist", "Matte Painter", "Technical Director"],
        "Weta Digital": ["VFX Artist", "3D Animator", "Compositor", "Concept Artist", "Creature Technical Director", "Rigging Artist", "Animation Supervisor", "FX Supervisor"],
        "DNEG": ["VFX Artist", "3D Modeler", "Compositor", "Roto Artist", "Paint Artist", "Matchmove Artist", "Layout Artist", "Environment Artist"],
        "MPC": ["VFX Artist", "3D Animator", "Compositor", "Matchmove Artist", "Layout Artist", "FX Artist", "Lighting Artist", "Creature Technical Director"],
        "Adobe": ["Software Engineer", "UX Designer", "Product Manager", "Marketing Specialist", "Graphic Designer", "Web Developer", "Video Editor", "Motion Graphics Designer"],
        "Autodesk": ["Software Engineer", "3D Modeler", "Product Designer", "Technical Support Specialist", "Simulation Engineer", "Product Manager", "Software Architect", "Technical Writer"],
        "Unity Technologies": ["Software Engineer", "Game Developer", "3D Artist", "Technical Artist", "VR/AR Developer", "Product Manager", "QA Tester", "Technical Support Engineer"],
        "Epic Games": ["Software Engineer", "Game Developer", "3D Artist", "Technical Artist", "UX Designer", "Product Manager", "Marketing Specialist", "Community Manager"],
        "Blizzard Entertainment": ["Game Developer", "Software Engineer", "3D Artist", "Level Designer", "Game Designer", "Producer", "QA Tester", "Community Manager"],
        "Electronic Arts (EA)": ["Game Developer", "Software Engineer", "3D Artist", "Animator", "Game Designer", "Producer", "Marketing Specialist", "Data Analyst"],
        "Ubisoft": ["Game Developer", "Software Engineer", "3D Artist", "Level Designer", "Game Designer", "Producer", "QA Tester", "Community Manager"],
        "Activision": ["Game Developer", "Software Engineer", "3D Artist", "Animator", "Game Designer", "Producer", "Marketing Specialist", "Data Analyst"],
        "Nintendo": ["Game Developer", "Software Engineer", "Hardware Engineer", "Game Designer", "Sound Designer", "Artist", "Producer", "QA Tester"],
        
    }

    recommended_jobs = []
    for company, jobs in companies_and_jobs.items():
        for job in jobs:
            if any(skill in job.lower() for skill in skills) or any(skill in company.lower() for skill in skills):
                recommended_jobs.append((company, job))

    # Prioritize 3D animation/VFX if the user has the skill
    if "3d animation" in skills or "vfx" in skills:
        vfx_companies = ["Pixar", "DreamWorks Animation", "Industrial Light & Magic (ILM)", "Weta Digital", "DNEG", "MPC"]  # Add more VFX companies
        for company in vfx_companies:
            if company in companies_and_jobs:
                for job in companies_and_jobs[company]:
                    if (company, job) not in recommended_jobs:
                        recommended_jobs.append((company, job))

    return recommended_jobs

def search_jobs_online(skills):
    """Searches for jobs online using a hypothetical API (replace with a real API)."""
    api_url = "https://api.github.com/search/repositories"  # Replace with real job search API endpoint
    params = {"q": ",".join(skills)}  # Format skills for the API
    headers = {"Authorization": f"token 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"}  # Include your GitHub token (replace with your actual API key)

    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        job_data = response.json()  # Assuming the API returns JSON

        # Extract job info (adapt this to the real API's response structure)
        extracted_jobs = []
        for item in job_data["items"]:
            extracted_jobs.append(f"Possible Job: {item['name']} at {item['full_name']} ")  # Replace with actual job details

        return extracted_jobs

    except requests.exceptions.RequestException as e:
        print(f"Error searching online: {e}")
        return []

def main():
    first_name, qualifications, skills = get_user_info()
    recommendations = recommend_jobs(skills)

    print(f"\nOkay, {first_name}, here are some job recommendations for you:")
    if recommendations:
        for company, job in recommendations:
            print(f"- **{company}:** {job}")
    else:
        print("I'm searching online for more options...")
        online_recommendations = search_jobs_online(skills)
        if online_recommendations:
            print("\nHere are some jobs I found online:")
            for job_info in online_recommendations:
                print(f"- {job_info}")
        else:
            print("I'm sorry, I couldn't find any suitable jobs online either.")
            print("Here are some suggestions to improve your chances:")
            print("  - Consider adding more skills to your profile.")
            print("  - Explore related fields or industries.")
            print("  - Keep learning and expanding your skillset!")

    print("\nI hope this helps! Feel free to ask if you have any other questions.")

if __name__ == "__main__":
    main()