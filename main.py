from typing import Counter
from text_rank import TextRank4Keyword

def texts():
    paragraphs = [
            '''
            Cryptocurrency “cannot come at great cost to the environment,” the electric carmaker said in a statement tweeted by Musk. The statement was hedged, but only slightly, with praise for crypto’s “promising future” and a promise to investigate less energy-hungry networks than Bitcoin’s.

            Bitcoin, a proof-of-work (PoW) blockchain reliant on energy-intensive mining units, has come under fire from environmental groups as its price has surged to all-time highs. The second-largest cryptocurrency by market cap, ether, also relies on PoW but is in the process of switching to proof-of-stake.

            Tesla’s pledge turns up the heat on the race to move bitcoin away from fossil fuels. The company’s decision to accept bitcoin was a watershed moment for corporate bitcoin adoption. Tesla’s turnabout on environmental matters will likely give fuel to the social and even political moment clamoring for change to the world’s largest cryptocurrency by market cap.

            The sudden freeze of Tesla’s bitcoin payments hands a decisive win to bitcoin’s energy critics. But it does not spell doom for Tesla’s remaining bitcoin investment nor its crypto experiment. “Tesla will not be selling any bitcoin,” the statement read. “We intend to use it for transactions as soon as mining transitions to more sustainable energy.”

            Tesla did test the liquidity of the bitcoin market with a $272 million sell announced during its most recent earnings call.
            ''',
            '''
            When most people hear the term artificial intelligence, the first thing they usually think of is robots. That's because big-budget films and novels weave stories about human-like machines that wreak havoc on Earth. But nothing could be further from the truth.


            Artificial intelligence is based on the principle that human intelligence can be defined in a way that a machine can easily mimic it and execute tasks, from the most simple to those that are even more complex. The goals of artificial intelligence include mimicking human cognitive activity. Researchers and developers in the field are making surprisingly rapid strides in mimicking activities such as learning, reasoning, and perception, to the extent that these can be concretely defined. Some believe that innovators may soon be able to develop systems that exceed the capacity of humans to learn or reason out any subject. But others remain skeptical because all cognitive activity is laced with value judgments that are subject to human experience.

            As technology advances, previous benchmarks that defined artificial intelligence become outdated. For example, machines that calculate basic functions or recognize text through optical character recognition are no longer considered to embody artificial intelligence, since this function is now taken for granted as an inherent computer function.

            AI is continuously evolving to benefit many different industries. Machines are wired using a cross-disciplinary approach based on mathematics, computer science, linguistics, psychology, and more.
            ''',
            '''
            The applications for artificial intelligence are endless. The technology can be applied to many different sectors and industries. AI is being tested and used in the healthcare industry for dosing drugs and different treatment in patients, and for surgical procedures in the operating room.

            Other examples of machines with artificial intelligence include computers that play chess and self-driving cars. Each of these machines must weigh the consequences of any action they take, as each action will impact the end result. In chess, the end result is winning the game. For self-driving cars, the computer system must account for all external data and compute it to act in a way that prevents a collision.
            ''',
            '''
            Artificial intelligence also has applications in the financial industry, where it is used to detect and flag activity in banking and finance such as unusual debit card usage and large account deposits—all of which help a bank's fraud department. Applications for AI are also being used to help streamline and make trading easier. This is done by making supply, demand, and pricing of securities easier to estimate.
            ''',
            '''
            Artificial intelligence can be divided into two different categories: weak and strong. Weak artificial intelligence embodies a system designed to carry out one particular job. Weak AI systems include video games such as the chess example from above and personal assistants such as Amazon's Alexa and Apple's Siri. You ask the assistant a question, it answers it for you.

            Strong artificial intelligence systems are systems that carry on the tasks considered to be human-like. These tend to be more complex and complicated systems. They are programmed to handle situations in which they may be required to problem solve without having a person intervene. These kinds of systems can be found in applications like self-driving cars or in hospital operating rooms.
            ''',
            '''
            Since its beginning, artificial intelligence has come under scrutiny from scientists and the public alike. One common theme is the idea that machines will become so highly developed that humans will not be able to keep up and they will take off on their own, redesigning themselves at an exponential rate.

            Another is that machines can hack into people's privacy and even be weaponized. Other arguments debate the ethics of artificial intelligence and whether intelligent systems such as robots should be treated with the same rights as humans.
            ''',
            '''
            elf-driving cars have been fairly controversial as their machines tend to be designed for the lowest possible risk and the least casualties. If presented with a scenario of colliding with one person or another at the same time, these cars would calculate the option that would cause the least amount of damage.

            Another contentious issue many people have with artificial intelligence is how it may affect human employment. With many industries looking to automate certain jobs through the use of intelligent machinery, there is a concern that people would be pushed out of the workforce. Self-driving cars may remove the need for taxis and car-share programs, while manufacturers may easily replace human labor with machines, making people's skills more obsolete.
            ''',
            '''
            Software Requirements
            The Software Requirements KA is concerned with the elicitation, negotiation, analysis, specification, and validation of software requirements. It is widely acknowledged within the software industry that software engineering projects are critically vulnerable when these activities are performed poorly. Software requirements express the needs and constraints placed on a software product that contribute to the solution of some real-world problems.

            Software Design
            Design is defined as both the process of defining the architecture, components, interfaces, and other characteristics of a system or component and the result of [that] process (IEEE 1991). The Software Design KA covers the design process and the resulting product. The software design process is the software engineering life cycle activity in which software requirements are analyzed in order to produce a description of the software’s internal structure and its behavior that will serve as the basis for its construction. A software design (the result) must describe the software architecture – that is, how software is decomposed and organized into components and the interfaces between those components. It must also describe the components at a level of detail that enables their construction.
            ''',
            '''
            Software Construction
            Software construction refers to the detailed creation of working software through a combination of detailed design, coding, unit testing, integration testing, debugging, and verification. The Software Construction KA includes topics related to the development of software programs that will satisfy their requirements and design constraints. This KA covers software construction fundamentals; managing software construction; construction technologies; practical considerations; and software construction tools.
            ''',
            '''
            Software Testing
            Testing is an activity performed to evaluate product quality and to improve it by identifying defects. Software testing involves dynamic verification of the behavior of a program against expected behavior on a finite set of test cases. These test cases are selected from the (usually very large) execution domain. The Software Testing KA includes the fundamentals of software testing; testing techniques; human-computer user interface testing and evaluation; test-related measures; and practical considerations.
            '''
    ]
    return paragraphs


def run():
    paragraphs = texts()
    print(len(paragraphs))
    Counter = 1
    for x in paragraphs:
        print("\nTest case #", Counter,": ")
        print("_________________________________________\n")
        tr4w = TextRank4Keyword()
        tr4w.analyze(x, candidate_pos = ['NOUN', 'PROPN'], window_size=4, lower=False)
        tr4w.get_keywords(20)
        Counter += 1
run()

