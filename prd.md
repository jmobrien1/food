# **Gastronomic Logic Systems: A Comprehensive Framework for the Chef de Cuisine Protocol and Technical Infrastructure**

The modern culinary landscape is defined by a widening chasm between the hyper-specialized techniques of Michelin-starred gastronomy and the pragmatic constraints of the domestic kitchen. While professional kitchens operate with specialized equipment, rigid hierarchies, and standardized protocols, the home environment often lacks the temporal and infrastructural resources required to execute high-level culinary intent. The Chef de Cuisine initiative represents a paradigm shift from traditional recipe-based applications toward a logic-driven architectural framework. By utilizing advanced Generative AI and Retrieval-Augmented Generation (RAG) strategies, this platform facilitates the translation of professional gastronomic theory into an actionable, constraint-aware execution plan for the home cook. The following analysis provides an exhaustive Product Requirements Document and Technical Roadmap for the realization of this system.

## **Document 1: The Product Requirements Document (PRD)**

The foundational premise of the Chef de Cuisine platform is that gastronomy is not a collection of static instructions but a dynamic system of logic. To bridge the gap between professional and amateur execution, the product must prioritize the transformation of intent through a multi-stage translation protocol. This necessitates a deep understanding of the user ecosystem, the technical limitations of domestic hardware, and the psychological drivers of the aspirational home cook.

### **Strategic User Archetypes and Persona Analysis**

The success of a high-end culinary logic engine depends on its ability to serve distinct user behaviors. Research into high-end culinary app usage suggests that users typically fall into two primary categories: those seeking technical mastery and those seeking logistical excellence in hospitality.1

#### **The Ambitious Amateur: The Pursuit of Mastery**

The Ambitious Amateur is defined by a desire to master professional techniques, often investing in high-end tools such as immersion circulators, chamber vacuum sealers, or specialized knives.2 For this user, the app serves as a digital mentor, providing the "why" behind the "how." They are less concerned with speed and more focused on the precision of the final result. Their primary motivation is the acquisition of "Chef's Secrets"—the subtle refinements that elevate a dish from amateur to professional.3 This persona requires deep-dive technical explanations and is likely to spend significant time in the "Audit" and "Chef's Secret" phases of the protocol.

#### **The Dinner Party Host: The Orchestrator of Experience**

The Dinner Party Host operates under a different set of constraints, primarily focused on the logistical complexity of multi-course service and guest satisfaction.1 This user often experiences "the weeds" (a professional term for being overwhelmed by tasks) and requires the app to function as a digital Sous Chef.6 The Host values the "Mise en Place" timeline above all else, requiring a system that can manage dietary restrictions, allergy risks, and the synchronization of disparate dishes to ensure a seamless service.5 Their success is measured by their ability to remain present with guests while delivering a menu of Michelin-level quality.5

| Feature Priority | The Ambitious Amateur | The Dinner Party Host |
| :---- | :---- | :---- |
| **Translation Engine** | High (Technique focus) | Moderate (Intent focus) |
| **Mise en Place Timeline** | Moderate (Learning focus) | Critical (Logistical focus) |
| **Dynamic Substitution** | High (Creative exploration) | High (Dietary management) |
| **Chef’s Secrets** | Critical (Skill acquisition) | Moderate (Presentation focus) |
| **Audit & Constraint** | High (Equipment optimization) | Critical (Time management) |

### **Core Functional Requirements: The Translation Protocol**

The heart of the Chef de Cuisine app is the Michelin Home Kitchen Translation Protocol. This four-stage logic engine ensures that every generated plan is physically possible within the user's specific environment while maintaining the integrity of professional standards.

#### **The Audit: Systematic Constraint Mapping**

The Audit is the diagnostic entry point of the application. It moves beyond a simple ingredient list to a comprehensive mapping of the culinary environment. Research indicates that the primary failure point in home gastronomy is the lack of specialized equipment or the miscalculation of time.8 The Audit mandates the input of available hardware (e.g., "cast iron skillet and a standard convection oven"), time limits, and user skill level.

This process must also account for "passive time"—the duration ingredients require to reach specific states, such as tempering meat or defrosting dough.6 The logic engine uses this audit to filter professional techniques. For instance, if a Michelin source text requires a pacojet for a specific sorbet, the Audit identifies the lack of this tool and instructs the Translation Engine to substitute it with a high-speed blender or a manual granita technique, preserving the flavor profile while adapting the texture-generation method.

#### **The Scale: Gram-Based Precision and Non-Linear Yield Adjustment**

Professional gastronomy relies on weight-based measurements to ensure consistency, a practice often neglected in domestic cooking.10 The Scale module of the Chef de Cuisine platform converts all recipe inputs into grams, utilizing a Conversion Factor (![][image1]) to adjust yields:

![][image2]  
However, the protocol recognizes that scaling is rarely linear. Spices, leavening agents, and reduction bases often require non-linear adjustments to avoid overpowering the dish or failing to achieve proper concentration.10 The logic engine applies "safety ceilings" to potent ingredients, a standard practice in professional recipe management.12

#### **The Translation Engine: Converting Intent to Execution**

The Translation Engine is the primary intelligence layer. It takes a high-level intent (e.g., "Chicken and Potatoes") and runs it through the audited constraints to produce a Michelin execution plan.13 If the Audit reveals a sous-vide setup, the engine might suggest a "Sous-vide Chicken Roulade with Pommes Purée." If the Audit identifies only a cast iron skillet, the engine translates this into a "Butter-Basted Pan-Roasted Airline Breast with Crispy Potato Pavé."

This translation preserves the "gastronomic core" of the dish—acid balance, fat content, salt levels, and textural crunch—while modifying the "mechanical execution" to suit the available tools.4 The engine draws from a library of professional texts (CIA, Michelin Guides) to ensure that even the simplified techniques adhere to the highest standards of culinary science, such as the Maillard reaction and proper protein denaturing.3

#### **Dynamic Substitution: Flavor Affinity Logic**

One of the most innovative features is the Dynamic Substitution engine, which utilizes the logic of *The Flavor Bible*. Rather than 1:1 ingredient swaps based on utility, the system suggests substitutes based on flavor affinities.16 This is calculated using Jaccard similarity across flavor profiles:

![][image3]  
This enables the app to suggest substitutes that maintain the "soul" of a dish. For example, if a recipe calls for tarragon but the user lacks it, the engine might suggest chervil or anise-seed depending on the other ingredients in the Audit, ensuring the "anise-like" profile is preserved.18 This multi-criteria decision-making process is essential for maintaining Michelin-level complexity in the face of domestic ingredient scarcity.20

#### **The Mise en Place Timeline: Algorithmic Temporal Planning**

The "Mise en Place" feature generates a minute-by-minute schedule that mimics the workflow of a professional kitchen.8 This "Mise en Temps" logic identifies "hands-off time"—such as baking, marinating, or resting—and populates those gaps with active tasks.6

The timeline is divided into three distinct phases:

1. **The Day Before**: Prep of long-term items such as stocks, infusions, or fermentations.8  
2. **The Hour Before**: Active station setup, pre-heating equipment, and final chopping.6  
3. **Active Cooking**: The service phase, where the app provides real-time guidance on timing, such as "Baste the steak now" or "Rest the protein for 10 minutes".14

### **UX/UI Journey: From Constraint to Plating**

The user journey is designed to reduce cognitive load while maximizing culinary output. The interface must be "kitchen-proof," prioritizing large touch targets and voice-activated commands to accommodate users with busy hands.2

1. **Input Phase**: The user performs the "Audit," selecting ingredients (or snapping a photo) and equipment. The app confirms the time limit.  
2. **Idea Generation**: The user enters a concept or selects from AI-suggested themes. The Translation Engine presents 2-3 Michelin-level execution paths based on the Audit.  
3. **The Prep List**: The app generates a categorized "Mise en Place" list, showing exactly what needs to be cut, measured, and prepped before the first heat is applied.8  
4. **The Timeline View**: An interactive, scrollable schedule. As the user completes tasks, the AI adjusts the remaining schedule in real-time.  
5. **Service Mode**: A high-contrast, voice-enabled mode that guides the user through the final assembly and plating, offering "Chef's Secrets" for finishing touches like micro-herbs or silkier sauces.14

## **Document 2: The Technical Roadmap (AI & Architecture)**

Building a logic engine that bridges professional gastronomy and home constraints requires a sophisticated technical infrastructure. The system must move beyond standard LLM patterns into a hybrid architecture that combines the semantic flexibility of vector search with the deterministic logic of a knowledge graph.23

### **Data Ingestion Strategy: The Hybrid RAG Framework**

The ingestion of the culinary library—including *The Flavor Bible* and the Michelin Home Kitchen Translation Protocol—cannot rely on a single data structure. Professional culinary data is a mixture of unstructured prose (guides), semi-structured data (flavor charts), and rigid logic (scaling and safety protocols).

#### **Vector Embeddings for Semantic Discovery**

Unstructured text, such as descriptive passages in Michelin guides or historical context from CIA textbooks, is indexed in a vector database (e.g., Pinecone or Weaviate).24 This allows the AI to retrieve "thematic context," such as the characteristics of "Provençal style" or the "emotional undertones" of comfort food.13 Vector databases excel at high-speed semantic matching across large datasets, making them ideal for initial "inspiration" queries.23

#### **Knowledge Graphs for Deterministic Logic**

The "Translation Protocol" and flavor pairings require a knowledge graph (e.g., Neo4j).28 In this structure, ingredients and techniques are nodes, and affinities or dependencies are edges. A knowledge graph allows for "multi-hop reasoning," which is essential for culinary logic.30 For instance, the system can trace that:

* (Chicken) \-\> \-\> (Lemon)  
* (Lemon) \-\> \-\> (Microplane)  
* (Microplane) \-\> \-\> (Audit\_Constraint)  
* (System) \-\> \-\> (Zester or Fine Knife)

| Data Component | Best Storage Mechanism | Reason |
| :---- | :---- | :---- |
| **Michelin Guide Prose** | Vector Database (Pinecone) | Semantic similarity and thematic retrieval 23 |
| **Flavor Bible Pairings** | Knowledge Graph (Neo4j) | Structured relationship mapping and multi-hop reasoning 30 |
| **Scaling Protocols** | Relational DB (PostgreSQL) | Deterministic math and standardized conversions 32 |
| **User Pantry/Audit** | Document Store (MongoDB) | Flexible, frequently updated constraint sets |

### **The "Chef Logic" Chain-of-Thought: Multi-Agent Prompt Architecture**

To ensure the AI follows the specific source logic of "Audit \-\> Scale \-\> Mise en Place \-\> Chef's Secret," a multi-agent system prompt architecture is recommended.13 Rather than a single prompt, the system employs a "Chain-of-Thought" (CoT) reasoning loop where specialized agents handle different stages of the protocol.13

1. **The Auditor Agent**: This agent focuses purely on reconciling the user's intent with their constraints. It identifies what is "technically impossible" and flags it for the translation engine.6  
2. **The Gastronomic Logic Agent**: This agent uses the Knowledge Graph to retrieve flavor affinities and technique dependencies. It constructs the "core" of the Michelin dish.19  
3. **The Scheduler Agent**: This agent calculates the timeline. It applies "Hands-Off Time" logic to the task list, ensuring that active prep happens during passive cooking windows.6  
4. **The Executive Chef Agent**: The final layer that reviews the entire plan for "gastronomic integrity." It injects the "Chef's Secrets"—techniques like "Monte au Beurre" or the use of a "Chinois" sieve for silky textures—ensuring the final output matches the Michelin persona.13

### **Recommended Tech Stack for High-Performance Gastronomy**

The choice of tech stack is influenced by the need for real-time temporal adjustments and complex data traversals.

#### **Frontend: Flutter for Cross-Platform UI Consistency**

Flutter is recommended over React Native for its superior performance in rendering complex, animation-heavy UIs such as the "Master Timeline".35 Benchmarks show that Flutter maintains more consistent frame rates (60-120 FPS) and lower CPU usage than React Native, which is critical for a smooth user experience in a fast-paced kitchen environment.37 Flutter's "Impeller" rendering engine provides the headroom necessary for simultaneous timers and voice-recognition processing.36

#### **Backend: Python/FastAPI and LangChain Orchestration**

Python remains the industry standard for AI applications. FastAPI is selected for its high performance and native support for asynchronous operations, which are essential for multi-agent LLM chains.28 LangChain serves as the orchestration layer, connecting the LLMs (e.g., GPT-4o or Claude 3.5 Sonnet) with the Neo4j Knowledge Graph and the Pinecone Vector store.30

#### **Infrastructure: Fully Managed vs. Self-Hosted**

For the initial rollout, managed services like Pinecone (for vector search) and Neo4j Aura (for the graph) are recommended to minimize operational overhead.24 These services handle scaling and reliability automatically, allowing the development team to focus on refining the culinary logic.25

### **Phased Rollout and Implementation Strategy**

The development of Chef de Cuisine is structured into three phases to manage technical risk and ensure the accuracy of the culinary translations.

#### **Phase 1: The Core Logic MVP (Text-Based Execution)**

The MVP focuses on the implementation of the Hybrid RAG architecture and the text-based generation of Michelin execution plans.

* **Key Deliverable**: A text-based interface where users input constraints and receive a "Translation Protocol" output.  
* **Technical Focus**: Establishing the Neo4j Knowledge Graph from the primary source texts and building the foundational LangChain "Chef Logic" chains.28  
* **Evaluation**: Human-in-the-loop verification by professional chefs to ensure the "Translation Engine" correctly identifies technique substitutes.

#### **Phase 2: Multi-Modal Intake (Computer Vision Integration)**

Phase 2 introduces image recognition to automate the "Audit" process, allowing users to snap photos of ingredients and equipment.22

* **Key Deliverable**: A "Digital Pantry" feature that uses computer vision to identify items and suggest potential Michelin dishes.  
* **Technical Focus**: Integration of specialized food recognition APIs (e.g., Calorie Mama or LogMeal), which currently show significantly higher accuracy (63%) for food items compared to general-purpose tools like Google Vision (9%).42  
* **User Value**: Reduced friction in the Audit phase, making the app more accessible for daily use.

#### **Phase 3: The "Mastery" Layer (Chef's Secrets & Techniques)**

The final phase focuses on the ingestion of specific "Michelin Secrets" and the refinement of the "Chef's Secret" logic.

* **Key Deliverable**: A library of "Technique Masterclasses" integrated into the execution plan, featuring specialized tips on plating, seasoning, and texture refinement.3  
* **Technical Focus**: Using LLMs to extract high-level "finishing techniques" from the library—such as "tempering" cold cream to prevent breaking or using "acid balance" to cut through fat.15  
* **User Value**: This phase fulfills the "mastery" promise for the Ambitious Amateur, providing the level of detail found in the world's finest kitchens.

## **Bonus: Distinctive Branding for the Mastery Ecosystem**

The following names have been selected to evoke a sense of mastery, professional guidance, and culinary precision without infringing on existing Michelin trademarks.46

1. **Affinities**: Directly references the core logic of flavor pairings and suggests a deep, intuitive understanding of ingredients.  
2. **Epure**: From the French *Épure* (to refine or draw in outline), signaling the refinement of home cooking and the precision of the translation engine.  
3. **Mise**: A short, punchy reference to *Mise en Place*, signaling the app's focus on professional organization and logistical excellence.  
4. **The Pass**: Refers to the area in a professional kitchen where the chef inspects dishes before they reach the guest, suggesting a final seal of quality and mastery.  
5. **Vanguard Chef**: Positions the app as a leader in culinary technology, bridging the gap between tradition and future-facing gastronomy.

## **Conclusion and Strategic Outlook**

The Chef de Cuisine platform is not merely a recipe application; it is a gastronomic translation layer that operationalizes high-level culinary theory for the domestic environment. By moving toward a logic-driven model, the system addresses the primary failure points of home cooking—lack of organization, technique mismatch, and ingredient limitations. The integration of a Hybrid RAG architecture ensures that the AI's suggestions are both semantically relevant and technically feasible.

Through the rigorous application of the "Audit, Scale, Mise en Place, and Chef's Secret" protocol, the platform provides the Ambitious Amateur with the tools for skill acquisition and the Dinner Party Host with the logistical support for hospitality excellence. As the platform evolves into multi-modal recognition and deeper technique extraction, it will become the definitive digital companion for those seeking to bridge the gap between their home kitchen and the world of Michelin-starred gastronomy. The technical infrastructure, grounded in GraphRAG and high-performance cross-platform frameworks, provides a scalable foundation for this future. The ultimate goal is to democratize the logic of the elite kitchen, ensuring that professional standards are no longer defined by the hardware in the room, but by the intelligence of the execution plan.

#### **Works cited**

1. Host the perfect dinner party \- Google Play, accessed February 17, 2026, [https://play.google.com/store/apps/editorial?id=mc\_apps\_editorial\_category\_essential\_host\_a\_great\_dinner\_party\_fcp](https://play.google.com/store/apps/editorial?id=mc_apps_editorial_category_essential_host_a_great_dinner_party_fcp)  
2. Bringing people together virtually through communal cooking | by Jaime Huang, accessed February 17, 2026, [https://uxdesign.cc/julienne-cook-alongside-those-closest-to-you-650342426e9f](https://uxdesign.cc/julienne-cook-alongside-those-closest-to-you-650342426e9f)  
3. The Ultimate Fish Hack: Michelin Star Secrets from Sadler Restaurant \- Lemon8, accessed February 17, 2026, [https://www.lemon8-app.com/@nahmj16/7585679301236851207?region=sg](https://www.lemon8-app.com/@nahmj16/7585679301236851207?region=sg)  
4. How to Cook Like a Top Chef, accessed February 17, 2026, [https://kruton.by/upload/blog/181.pdf](https://kruton.by/upload/blog/181.pdf)  
5. After 15 years in professional kitchens, I built an app that plans your ..., accessed February 17, 2026, [https://www.reddit.com/r/iosapps/comments/1n5lhna/after\_15\_years\_in\_professional\_kitchens\_i\_built/](https://www.reddit.com/r/iosapps/comments/1n5lhna/after_15_years_in_professional_kitchens_i_built/)  
6. Mise En Temps- Timeline Like A Baker | The Black Hat Baker, accessed February 17, 2026, [https://theblackhatbaker.com/2018/03/11/mise-en-temps-timeline-like-a-baker/](https://theblackhatbaker.com/2018/03/11/mise-en-temps-timeline-like-a-baker/)  
7. The Gourmet Host | Dinner Party Planning Tools, accessed February 17, 2026, [https://thegourmethost.com/](https://thegourmethost.com/)  
8. Culinary Basics: Mise En Place \- National CACFP Association, accessed February 17, 2026, [https://www.cacfp.org/2024/05/07/culinary-basics-mise-en-place/](https://www.cacfp.org/2024/05/07/culinary-basics-mise-en-place/)  
9. Mise en Place \- The Culinary Pro, accessed February 17, 2026, [https://www.theculinarypro.com/mise-en-place-savory](https://www.theculinarypro.com/mise-en-place-savory)  
10. Mastering Recipe Scaling for Professional Chefs | CalcMenu, accessed February 17, 2026, [https://www.calcmenu.com/en/blog-en/mastering-recipe-scaling-for-professional-chefs/](https://www.calcmenu.com/en/blog-en/mastering-recipe-scaling-for-professional-chefs/)  
11. How To Scale Up A Recipe: 4 Easy Steps | Cook's Delight, accessed February 17, 2026, [https://www.cooksdelight.com/blog/4-easy-steps-to-scale-up-a-recipe-for-foodservice-menus/](https://www.cooksdelight.com/blog/4-easy-steps-to-scale-up-a-recipe-for-foodservice-menus/)  
12. Recipe Conversion \- The Culinary Pro, accessed February 17, 2026, [https://www.theculinarypro.com/recipe-conversion](https://www.theculinarypro.com/recipe-conversion)  
13. ChatGPT Prompt of the Day: "The 3-Michelin Star Chef's ... \- Reddit, accessed February 17, 2026, [https://www.reddit.com/r/ChatGPTPromptGenius/comments/1hyhzze/chatgpt\_prompt\_of\_the\_day\_the\_3michelin\_star/](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1hyhzze/chatgpt_prompt_of_the_day_the_3michelin_star/)  
14. Embark on a Culinary Journey: Explore International Cuisines \- Nicol Retailer, accessed February 17, 2026, [https://nicolretailer.com/blog/](https://nicolretailer.com/blog/)  
15. Delicious Butter Chicken ( Murgh makhani) recipe, accessed February 17, 2026, [https://www.hassanchef.com/2019/10/delicious-butter-chicken-murgh-makhani.html](https://www.hassanchef.com/2019/10/delicious-butter-chicken-murgh-makhani.html)  
16. The Flavor Bible The Essential Guide To Culinary C, accessed February 17, 2026, [https://ftp.fosswaterwayseaport.org/book-search/0Him9x/7GF253/TheFlavorBibleTheEssentialGuideToCulinaryC.pdf](https://ftp.fosswaterwayseaport.org/book-search/0Him9x/7GF253/TheFlavorBibleTheEssentialGuideToCulinaryC.pdf)  
17. Flavor Bible Report \- RPubs, accessed February 17, 2026, [https://rpubs.com/areeves87/389547](https://rpubs.com/areeves87/389547)  
18. The Flavor Network, accessed February 17, 2026, [https://flavorpair.me/](https://flavorpair.me/)  
19. The Flavor Network | brege.org, accessed February 17, 2026, [https://brege.org/post/the-flavor-network/](https://brege.org/post/the-flavor-network/)  
20. Artificial Intelligence-Enabled Ingredient Substitution in Food Systems: A Review and Conceptual Framework for Sensory, Functional, Nutritional, and Cultural Optimization \- PMC, accessed February 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12651232/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12651232/)  
21. Understanding mise en place: What is mise en place? \- Culinary Arts Academy, accessed February 17, 2026, [https://www.culinaryartsswitzerland.com/en/news/understanding-mise-en-place-what-mise-en-place/](https://www.culinaryartsswitzerland.com/en/news/understanding-mise-en-place-what-mise-en-place/)  
22. Automatic Image Recognition Meal Reporting Among Young Adults: Randomized Controlled Trial \- JMIR mHealth and uHealth, accessed February 17, 2026, [https://mhealth.jmir.org/2025/1/e60070](https://mhealth.jmir.org/2025/1/e60070)  
23. Knowledge graph vs. vector database for RAG: which is best?, accessed February 17, 2026, [https://www.meilisearch.com/blog/knowledge-graph-vs-vector-database-for-rag](https://www.meilisearch.com/blog/knowledge-graph-vs-vector-database-for-rag)  
24. How do I choose between Pinecone, Weaviate, Milvus, and other vector databases?, accessed February 17, 2026, [https://milvus.io/ai-quick-reference/how-do-i-choose-between-pinecone-weaviate-milvus-and-other-vector-databases](https://milvus.io/ai-quick-reference/how-do-i-choose-between-pinecone-weaviate-milvus-and-other-vector-databases)  
25. Best Vector Databases in 2025: A Complete Comparison Guide \- Firecrawl, accessed February 17, 2026, [https://www.firecrawl.dev/blog/best-vector-databases-2025](https://www.firecrawl.dev/blog/best-vector-databases-2025)  
26. ChatGPT Prompt of the Day: MICHELIN STAR MEDITERRANEAN CHEF EXTRAORDINAIRE : r/ChatGPTPromptGenius \- Reddit, accessed February 17, 2026, [https://www.reddit.com/r/ChatGPTPromptGenius/comments/1jhlh3i/chatgpt\_prompt\_of\_the\_day\_michelin\_star/](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1jhlh3i/chatgpt_prompt_of_the_day_michelin_star/)  
27. Vector Database vs. Knowledge Graph: Making the Right Choice When Implementing RAG, accessed February 17, 2026, [https://www.cio.com/article/1308631/vector-database-vs-knowledge-graph-making-the-right-choice-when-implementing-rag.html](https://www.cio.com/article/1308631/vector-database-vs-knowledge-graph-making-the-right-choice-when-implementing-rag.html)  
28. RAG Tutorial: How to Build a RAG System on a Knowledge Graph \- Neo4j, accessed February 17, 2026, [https://neo4j.com/blog/developer/rag-tutorial/](https://neo4j.com/blog/developer/rag-tutorial/)  
29. LangChain-Neo4j Partner Package: Officially Supported GraphRAG, accessed February 17, 2026, [https://neo4j.com/blog/developer/langchain-neo4j-partner-package-graphrag/](https://neo4j.com/blog/developer/langchain-neo4j-partner-package-graphrag/)  
30. GraphRAG Explained: Building Knowledge-Grounded LLM Systems with Neo4j and LangChain | by DhanushKumar | Dec, 2025 | Towards AI, accessed February 17, 2026, [https://pub.towardsai.net/graphrag-explained-building-knowledge-grounded-llm-systems-with-neo4j-and-langchain-017a1820763e](https://pub.towardsai.net/graphrag-explained-building-knowledge-grounded-llm-systems-with-neo4j-and-langchain-017a1820763e)  
31. Implementing 'From Local to Global' GraphRAG With Neo4j and LangChain: Constructing the Graph, accessed February 17, 2026, [https://neo4j.com/blog/developer/global-graphrag-neo4j-langchain/](https://neo4j.com/blog/developer/global-graphrag-neo4j-langchain/)  
32. Converting and Adjusting Recipes and Formulas – Basic Kitchen and Food Service Management \- BCcampus Open Publishing, accessed February 17, 2026, [https://opentextbc.ca/basickitchenandfoodservicemanagement/chapter/convert-and-adjust-recipes-and-formulas/](https://opentextbc.ca/basickitchenandfoodservicemanagement/chapter/convert-and-adjust-recipes-and-formulas/)  
33. Create a Neo4j GraphRAG Workflow Using LangChain and LangGraph, accessed February 17, 2026, [https://neo4j.com/blog/developer/neo4j-graphrag-workflow-langchain-langgraph/](https://neo4j.com/blog/developer/neo4j-graphrag-workflow-langchain-langgraph/)  
34. From Amateur Cook to Michelin Star: Bridging the Chasm Between AI Demos and Production Systems | by Bruno Sad | Dec, 2025 | Medium, accessed February 17, 2026, [https://medium.com/@brunon.sad/from-amateur-cook-to-michelin-star-bridging-the-chasm-between-ai-demos-and-production-systems-5025060e99d0](https://medium.com/@brunon.sad/from-amateur-cook-to-michelin-star-bridging-the-chasm-between-ai-demos-and-production-systems-5025060e99d0)  
35. Flutter vs React Native: Complete 2025 Framework Comparison Guide | Blog, accessed February 17, 2026, [https://www.thedroidsonroids.com/blog/flutter-vs-react-native-comparison](https://www.thedroidsonroids.com/blog/flutter-vs-react-native-comparison)  
36. Flutter vs React Native vs Native: 2025 Benchmark Comparison \- SynergyBoat, accessed February 17, 2026, [https://www.synergyboat.com/blog/flutter-vs-react-native-vs-native-performance-benchmark-2025](https://www.synergyboat.com/blog/flutter-vs-react-native-vs-native-performance-benchmark-2025)  
37. React Native vs Flutter: Which Saves More Development Time in 2025? \- Blott, accessed February 17, 2026, [https://www.blott.com/blog/post/react-native-vs-flutter-which-saves-more-development-time](https://www.blott.com/blog/post/react-native-vs-flutter-which-saves-more-development-time)  
38. What is the Performance of Flutter vs. Native vs. React-Native? \- TechAhead Software, accessed February 17, 2026, [https://www.techaheadcorp.com/blog/what-is-the-performance-of-flutter-vs-native-vs-react-native/](https://www.techaheadcorp.com/blog/what-is-the-performance-of-flutter-vs-native-vs-react-native/)  
39. Mobile-First Construction Apps: React Native vs Flutter Comparison | by AlterSquare, accessed February 17, 2026, [https://altersquare.medium.com/mobile-first-construction-apps-react-native-vs-flutter-comparison-75b2a5fadbbf](https://altersquare.medium.com/mobile-first-construction-apps-react-native-vs-flutter-comparison-75b2a5fadbbf)  
40. Best Vector Database For RAG In 2025 (Pinecone Vs Weaviate Vs Qdrant Vs Milvus Vs Chroma) | Digital One Agency, accessed February 17, 2026, [https://digitaloneagency.com.au/best-vector-database-for-rag-in-2025-pinecone-vs-weaviate-vs-qdrant-vs-milvus-vs-chroma/](https://digitaloneagency.com.au/best-vector-database-for-rag-in-2025-pinecone-vs-weaviate-vs-qdrant-vs-milvus-vs-chroma/)  
41. LogMeal's AI Food Recognition: A Validated 24-Hour Recall Alternative, accessed February 17, 2026, [https://blog.logmeal.com/logmeal-ai-food-recognition-a-24-hour-recall-alternative/](https://blog.logmeal.com/logmeal-ai-food-recognition-a-24-hour-recall-alternative/)  
42. (PDF) Use of different food image recognition platforms in dietary assessment: a comparison study. (Preprint) \- ResearchGate, accessed February 17, 2026, [https://www.researchgate.net/publication/346075674\_Use\_of\_different\_food\_image\_recognition\_platforms\_in\_dietary\_assessment\_a\_comparison\_study\_Preprint](https://www.researchgate.net/publication/346075674_Use_of_different_food_image_recognition_platforms_in_dietary_assessment_a_comparison_study_Preprint)  
43. Use of Different Food Image Recognition Platforms in Dietary Assessment: Comparison Study \- PMC, accessed February 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7752530/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7752530/)  
44. Michelin Stars & AI: How Artificial Intelligence is Elevating Restaurant Experiences, accessed February 17, 2026, [https://www.entire-magazine.com/read-more/michelin-stars-amp-ai-how-artificial-intelligence-is-elevating-restaurant-experiences](https://www.entire-magazine.com/read-more/michelin-stars-amp-ai-how-artificial-intelligence-is-elevating-restaurant-experiences)  
45. Tabouli Salad (Tabbouleh) Recipe: Chef-Tested Perfection \- A Pure Palate, accessed February 17, 2026, [https://www.apurepalate.com/tabouli-salad-recipe/](https://www.apurepalate.com/tabouli-salad-recipe/)  
46. Super Sticky Brand Names Course \- Eat My Words, accessed February 17, 2026, [https://eatmywords.com/brand-names-course/](https://eatmywords.com/brand-names-course/)  
47. Crafting a Memorable Brand Name: Expert Tips by Liz Goodgold \- YouTube, accessed February 17, 2026, [https://www.youtube.com/watch?v=9\_tAgGpVdx8](https://www.youtube.com/watch?v=9_tAgGpVdx8)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAYCAYAAACBbx+6AAACGElEQVR4Xu2UP0hWURjGXxwsSAwDlxBMrE2xwQIbhJYQ/9Dk4FhCioOkBDa0RzapgwUZQuSkqEPm4OSiWwhFDiIIgjhEJWpSYj0P5xx5fb/zXe9nk3B/8OO793nPufd+99zzimRkJFIEK+E1WOV/K2A5vHw86nSq4XP4Ga7Au6r2UB2TCymNwhv1wQn4F76GvfAZHPUZHyAfc+LGbIr7o4Eu+MHXrqi8EY74nE7BQfgCDsNJVUuEN4gNGhCX37AF0CKudgRLTY0k3TjUuMKWV5J/3jFrkn8Q812T1fq8weQarlTsmnzIpD9DfthA0yFuMpfVcklcbUllJT57r7IYdfCTDUG/uPlbKuOfKFbns+o4h1VxF+i0BbAuuW9iO5LFuAObbCju7XF+t8qG1PGphOWp9zaL2zB/4IwaF+DYDRsWAOfvw1Z4X1J+s5rwwNZ5PcjDdscad/NZsfcJpuKqxCd89RmXVfPI5/dMnpbb4uZz0wYuwml1nsgbcRd4Z3L2ReYLJn/s8zKTW7iBntgQfJTcl3ML1pgsL+HtXjf5L5+PmTx0jXaTW9gmY8RWsyA4OdbOwoVf2oK4fNyGBnaeGJyr21lBhAbO79ISHvipP99RtQe+dlNlgbfwmw09/FY5r8cW0rAHf8Lv4h6Gn0CbqnOzsV8ewkVx7U4TNg/l/AP4RU42/8CyuDYW7sff3/Kfn0ZGRkbGOeUf8nqXOFI4hu4AAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAA+CAYAAACWTEfwAAAJlUlEQVR4Xu3dechtVRnH8acy00YzMyzrvg2OZRMFlSVFBZlCWZgm6r2RWA4palgZlVFRQTZHWRkWZg5hZWpiRSIFNtCgZSmmhmODY+VUWevnWk/7Oc+7zvvu13Mu3nv5fuDh7PWsffZ+z/3nPqy91tpmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWOf9d0qcEE+ak51yYk78b14Ixx7bDqfZN1PfY0tsFPqXEr83zSlW+69KeQAAgJmpyDg85S5o+Yek/H31JKvX2z53zEkspHZI7Uj53drxl0ucHPqWc0OJv+VkousfmJMAAACzUpHxgJws/lPiLzk5g0fkxBzlAk3tvVLuwhJPTrmV0DUPy8kk/x0AAAAz28KmFxlfs+l965JDSxyUcvq7499+QDi+LzQyOObfYsw5AAAAK/KZEt/IyeYymyxANN/rthLnWy2Q3hj65FUlTi/x+RJ/Dnkd61qfS7krS3y2xB0l3lJidej3ex1T4ns2ea8n2vDo8dYSN4Y+d4bVc7Yu8fQS54W+15Q4q/VnR9jw+2K/z0/L9Bu+VOK0Et9vnwAAAHN1j01OzI/yKJWOF0Jbj0wjP/cF4Vhz1+TSEte3Y3mgTRZBOvaFDpu2/EJrS7yX+jZJ7Uxz75T/ndW5Z9H57TN/78cl/hnap5bYuB3rXBWj0b9KnBTaKjB3DG0AAIC5yEVLpD6NVMnjS9zZjlVsvbPEw1vbczr/Ta3tc+JWt0/1vaQdO+XOTjm524Z7bVPiLhvu9fwSl7RjN+03KJ/7Ni/xsBJbpj79PrU3s+H3aVTQqU+LGaJ87dwGAACY2VY2vcjQCkr1eeGlR4pnljikxK4hH91kQ5G0c8jv0XKZcs/JSat5v9eq1Hd7iT1D+2DrX1uU/3pONr+xOiLm9Pt0/tHW/335Hi/s5HIbAABgZldYv8h4kC3O/8DqyFSkkSh5qk2er8UK54a2+vZvxyoEZe+W71F+2r3yd9TWvLFzUn7f1tejx5zqU1Hm5+j3TTtf/LHqxe3zw1Z/g/PCUY9q9wl5AACAmajAuC7l9CiwV7gslPhgaKuA0hwv0aT7uMhAc7v06NH59U4MOc0t04hcjxYhxHu914Z7/SLkj7V67V1s8bWubX09R9nQp2JTFkJO9Ps0b05F3dNKvL/Ec0u8uPVr093j2rHPufu31bl4AAAAM9PKSi02UJHhhYbmianIeelw2iLak03f1XeOT32Xt7yKLS+C3EVWJ/O/KOR07u6hnfm9rrG69Ujkf/czS+zXjjUq6PTY9OYSt1i976tDn1M+F3Svbbne71NOj1EjXUP38lW2OufIoRsAAMzTg61OQn9cCxUI+ZHcNK+z+h+2NmX1eVvLba4KAACAFXpZiffYMEKkvb8+anX0RLnHDKf+nx6Jqe8dIad5TNozLI7c6No+gV/zurTv2adLfLHl8igPAAAAptDImoqn/ILyq1s+0vsk9RixRxvA6jFdFCe3Z3oUCQAAgBG0436vqMqjYJos3zvPbZcTxdts8W78/lJ1rU4EAADACD4JP/L3R65pbW3ZoHZvs1fX21dMI3KHh/ZHbNimwj8BAACwDBViPyrxDKubouo1RdqeQjvgu6usnpc3VV2OvqP3bGq14idae4y3jgwAAIANnr+mSK890grRVa2dR8vy49Ex/JVNKtj00vFvlfj7xBlrl/ZV+ylxv4YWmgAAgBn9wRYXYhd0cssVbNoL7H0pd5ZNfkd7hz0vtAEAADCCCqobOrlcnGlkLOciLUjIetcZ69KRAQAAsMFTQZXnguVCa2urryZSrjdCptcnPSsnrZ5/ek4CAABgnEOtvt9SRdWZJT4e+mLB9pOQV2Gm/IdKbFTi2Vbfo5lfx/Qpq68y0rl65BqvDQAAgDk5wOoigUfljuIQq/PT/GXg65uHlvhriT9afbWWCssjJs4Yb1VOjNAbpZyVF9knl9gttPNoqWhvvNinlb+PnDhjOv/3ui53BHpxfO++AAAAy9rMahHxytxRXGHT3+AwzWVWRx1X6oycmBMvvpxGNpXbJeREC0T+Edq3WV3FO9YpVheQLEX39RfDAwAAjKYi4qs52bzCar8e9a6PNA+xN6KlnEYTc24WY76vc3bISQAAgKVsaksXGtta7dcGv+uj662+VSLLjya12lcjbLNY6t9RtAHzcucAAAAsomJG8+6m2d9qkaENhEWLKa60+p7VO0p8ssTq1qfi793WL0o0qqQ5XPuUuN0mz7nT6gKPWDBpLtifWk5vl1hjtag6cTjlXnr/qq57kA1vnYjU1kKS7DAbzv1ViSeEPhV5mruXryWa33eR1b/n+JDf3vrnf6XE263+m/3S+ucAAAAsSQWEio1pNB/Ni4xjrb6lQXO1PKfPE9qxCivPRdraJOe8rdWyouJnu3b8AatzzlTs3NhycqD1r7NjOz6qtSO1p702TH2nWl2MED26xFbWv9YbUtvFfxOnV5ndHdrqPy20AQAAlqVVobnIiFToqP+HKa+ciqMezQu7POV0/utDey+rr8eKen9HzmlBwCWhrf64MfG1Ja4J7V4RFalvm5xs1OeFqLcVv7a6GOHW0Cfqi/v2HdNyUW4DAACMslQREUfXIuU00tajvlWdXKTrxkUMR9ricyTn1PZHsxu39p5D973tN6e2irZp8vWdXzuOzKn9sdDO8rX0loyYOzi1AQAARlMRsXlOFi+32rdTyu/d8tN437md3FJtPf6Mo24ahYvn7RHaGlXbJLSdt48Obc2d27nEFi3n9JaK/H333RL3tOOb2qfOzY9OvWiNK1F9JFFtf9wrmvunEBWsAAAAoz3F6iO+TAVH73GhiiUvYnq+0z7z40Sn95zmQkltjWbFAue3JW4O7Z+XuLoda3GD6HvaQ070G/y6+TPOg3Oau5b/Dqe8Fh2oKNyv5S62Oict+n37PMmGAs8dZ8P+dbtavab2ptN8wbWxQTAAANjAfdtqQXGO1aKoV8A5nbd7Tgbq1+PASCswNap0Xol9bXGhpNG4uGGt5PvoGspppajzhQG+2EHz57RyVaNnoteAaa6ZRgvdu6ze65YWWrGarSlxV4kLU16rSbWiVfc8O+S1klW5fC0VeDpfj201Uqlz4ivNAAAA1knaqqO3LxoAAADuJxpV8rleX7CVv+YKAAAAa9mWVud//cwmt/YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAuu5/HaLBkRhVfhcAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAA/CAYAAABdEJRVAAARM0lEQVR4Xu3dCbR95RjH8YcyFSGJovoTSWQoKVREpWWqRYkGrbQaVCgJIZQls0gDSajVnGmRRhXSYCjRQkgyJUnmqQzvt72fdZ/znHfve8793+G4/T5rveue99l7n2Gf+//v577TNhMREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREREVlo++ZA62GlrF3KOqU8ppS1SllSyr3CPovVDqXsmIMV9y7lvyl2v1KuTLG58MhSHm3Nd8P39IhSHjqwx+J1lQ3/Ht7Vps4Hhd/bR5WyZtyp9aocaD3WmmNEREQmzitzoLVLKcdbk5AcWcrupby6lH+0MRKTcXy6lP/k4DTYf48cnGMPKuX6HOzwTxtO2PD6Ut6Vg7OIZIXzwmufW8qepexVyuFt7IlTu47sb6WcnIM9NrT6Z59rb7Tms2YPsSbOe+Lcc04ob2hjW03teodbUh3rmhI2ERGZUF2tDfCELSNWi/f5tjUJ3zj+XsqyOTjHbivlPjlY8TzrPw9d8YwkyZ/nR9a0Eo2KY+6SYqu18XGRsC3JwR4vLeX8HJwH03222vba98TnXSPFHmdK2EREZEL1JVG1Cx264ovBqJ/r9lJOtO79zyvlPTkYbFDK73KwOLaUr+Vgh9pr38Pq8cVgf2taarusaPXPXvt9fao1yXn0eFPCJiIiE4qLYBcucvukGK0QxF+c4nSRfdeaFp71Q/z+1rQcxa7Xu1uTrNBdhdNLee3U5jtajS4pZfUQww2lPLh9TPffn0s5emrzgEOt6fbivdBdlp1kTWKUt70l1Ws2aX/uasOJgFvBurfhnTkQkHhMh89de/5flHJUDhaXlnJW+5jExG1Ryq9LeXKIPaWNbWRNAnizNd+v4xgSy+ibpVzQPqaFkq7az01tHsDYvxNK+WEpy5Ryt8HNds9SbirllBTn8/K704VW3HxOVm1j+TWQ96UrWQmbiIhMpNfkQIuELF/QntXG8oD8z5ZyYfv4BzZ4HHXEGK1THvN43E53VY79NMT+EOL5PYLkhKQAl9nwPtRJCu+btjHOaZTxXz4Wj8SG45kAUJNf1z2wlE1zcEzx3LlzSvl3iiHuF49jkD1JJz/j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>