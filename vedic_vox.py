import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import time

st.set_page_config(page_title="VEDIC VOX",layout="centered")


img_contact_form = Image.open(r"E:\ideation-vedicvox(sozoconnect)\vedicvoxbg.png")
# Club logo

# Navigation bar

      
app = option_menu(
                menu_title='VEDIC VOX ',
                options=['Home', 'About', 'Events', 'Resources', 'Membership', 'Contact'],
                icons = ['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill', 'envelope-fill'],
                menu_icon=" ",
                default_index=0,
                orientation="horizontal",
                styles={
                    "container": {"padding": "5!important","background-color":'navyblue'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "black"},
        "nav-link-selected": {"background-color": "red"},} 
        
                
                )


if app == "Home":
    with st.container():
        
        # Create columns with specified widths
        cols = st.columns(2)

        # Content for the first column
        with cols[0]:
            st.image(img_contact_form, width=300)

        # Content for the second column
        with cols[1]:
            # Club name
            st.title("VEDIC VOX")
            st.markdown("> Ideas Presentation Club")

            # Motive of the club
            st.markdown("""
                     [Vedic Vox ] is a platform for modern expression rooted in ancient wisdom. 
                    It empowers individuals to articulate ideas effectively and fosters innovation. 
                     It cultivates a community of creativity and collaboration.
                """)

    with st.container():
        tab1,tab2=st.tabs(["MOTIVE OF THE CLUB","GOALS OF THE CLUB"])
        with tab1:
            # Motive of the Club Section
            st.title("Motive of the Club")

            st.write(" The college landscape is filled with brilliant ideas, but strong communication skills are needed to bring them to life. An ideas presentation club acts as a launchpad, helping students transform their ideas into reality.")
   

        with tab2:
            st.title("Goals of the Club")
            st.write("The Ideas Presentation Club empowers students to transform their visions into reality. Here, we will effectively conduct:")
            st.write("- Dynamic discussions around Startup ideas and entrepreneurial ventures.")
            st.write("- Inspiring Ted talks and online podcasts where leading individuals promote compelling ideas and their journey with them.")
    with st.container():
        st.empty()

if app == "About":
    with st.container():
        tab1,tab2,tab3=st.tabs(["Mission and Vision of club "," Club Activities ","   CLUB LEADS "])
        with tab1:
            st.markdown(""" 
                        <h1 style='color:white ;'>Mission and Vision of the Club</h1>
                    """,unsafe_allow_html=True)
            st.write('''Our mission and vision encapsulate our unwavering dedication to nurturing a vibrant community driven by creativity, innovation, and personal growth. 
                      Here's a glimpse into our mission and vision
                      ''')


            st.markdown("""
            <style>
            .custom-bfont {
                font-family: Arial, sans-serif;
                font-weight: bold;
            }
            .custom-ifont {
                font-family: Arial, sans-serif;
                font-weight: italic;
                    
            }
            </style>
            """, unsafe_allow_html=True)

            st.markdown("""
            # <span class="custom-bfont">🚀 Mission</span>
            <span class="custom-ifont">Established in [2024], <font color=yellow> __Vedic Vox__</font> embarks on a bold mission to serve as a fertile ground where individuals can explore, articulate, and amplify their ideas. Our primary goal is to empower students to blossom into <font color=yellow> __confident communicators__</font> and<font color=yellow> __pioneering thinkers__</font> , arming them with the essential skills and mindset necessary to navigate the complexities of our ever-evolving world with unwavering clarity and purpose. Through a diverse spectrum of meticulously curated activities and initiatives,<font color= orange> __We endeavor to ignite the dormant spark of creativity within each member and foster a culture of collaboration, curiosity, and continuous growth__.</span>
            """, unsafe_allow_html=True)
            st.markdown("""
                         # <span class= "custom-bfont">🌟 Vision </span>
                        <span class= "custom-ifont"> At <font color=yellow> __Vedic Vox__</font>, our vision extends beyond the confines of mere imagination—<font>_we aspire to forge a dynamic and inclusive community where every voice is not only heard but celebrated, and where every idea holds the potential to catalyze profound change._ We envision a future where students hailing from diverse backgrounds converge to share their unique perspectives.By cultivating an environment steeped in <font color= yellow>__Lifelong Learning__</font>, <font color= yellow>__Boundless Empathy__</font>, and <font color= yellow>__Unwavering Empowerment__</font>, <font> we aim to nurture the leaders and trailblazers of tomorrow, poised to sculpt a world that is not just _harmonious_, but _Truly Transformative._</font> </span>""",unsafe_allow_html=True)
            st.write("  ")
            
            st.markdown(""" 
                          # <span class ="custom-bfont"> 💡</sapn> 
                        <span class="custom-ifont">Through our mission and vision, <font color =yellow> __Vedic Vox__</font> endeavors to inspire individuals to embrace the boundless depths of their creativity, to unlock the latent potential within, and to harness the transformative power of ideas. Together, we believe in crafting a future that shines with the brilliance of collective ingenuity—<font color = tangerine> ___ONE IDEA, ONE STEP, at a time.___</font>
                        </span>""",unsafe_allow_html=True)
        with tab2:
            with st.expander("Idea Presentation Sessions"):
                st.markdown(""" <font color =yellow>At __Vedic Vox__</font>, we organize regular idea presentation sessions where students have the opportunity to practice articulating their thoughts and ideas. These sessions provide a supportive environment for students to share their creative concepts and receive constructive feedback from peers. By participating in these sessions, students can enhance their <font color =yellow>__public speaking skills__</font>,<font color =yellow>  __build confidence__ </font> in expressing their ideas, and refine their <font color =yellow> __presentation techniques.__</font>
                """,unsafe_allow_html=True)
            with st.expander("Workshops on Entrepreneurship and Innovation"):
                st.markdown(""" Our club hosts workshops focused on <font color= orange> entrepreneurship and innovation</font>, providing students with practical skills and knowledge to turn their ideas into reality. <font>Through interactive sessions led by ___"industry experts"___ and  ___"seasoned entrepreneurs"___, students learn about the   ___"entrepreneurial mindset"___, startup development process, </font>and strategies for <font color =orange >___Turning innovative ideas into successful ventures___</font>. These workshops not only inspire students to think creatively but also equip them with the tools and resources needed to pursue entrepreneurial endeavors""",unsafe_allow_html=True)

            with st.expander("Guest Lectures"):
                st.markdown('''<font>We regularly invite guest speakers from various fields, including  <font color =tangerine >__"business"__,  __"technology"__, and __"academia"__</font>, to share their insights and experiences with our members.<font color= tangerine> These guest lectures provide valuable exposure to diverse perspectives and real-world examples of successful idea implementation.</font> By attending these lectures, students gain new insights, broaden their horizons, and cultivate a deeper understanding of the    __"challenges"__ and __"opportunities"__ in their areas of interest. </font>''', unsafe_allow_html=True)
               

            with st.expander("Collaborative Projects"):
                st.markdown('''<font color= red > __Vedic Vox__</font> facilitates collaborative projects where students can work together to explore innovative ideas and solutions to real-world problems. <font color =red>_Through teamwork and collaboration, students learn to leverage their collective strengths, brainstorm creative solutions, and execute projects effectively_</font>. These collaborative experiences not only foster critical thinking and problem-solving skills but also promote <font color= red>teamwork</font>, <font color= red>communication</font>, and <font color= red>leadership abilities</font>.''',unsafe_allow_html=True)
            
        with tab3:
            st.markdown('''
                    ## CORE MEMBERS and LEADERSHIP TEAM

                    Vedic Vox is being lead by  by <font color=#41C9E2> AMARNATH SILIVERI</font>, <font color=#41C9E2>SAI DEEKSHITHA ANDRA </font>, and [Advisor's Name]. 

                    > **AMARNATH SILIVERI**: A passionate person for idea sharing with a background in Data Science and tools to get insights from data.
                        
                    > **SAI DEEKSHITHA ANDRA**: Brings expertise in [specific area].
                        
                    > **Advisor's Name**: Provides guidance based on their experience in [related field].

                    ### Together, they lead the club with dedication and enthusiasm.
                    ''',unsafe_allow_html=True)            
