import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import time

st.set_page_config(page_title="VEDIC VOX",layout="centered",page_icon="🚀")


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
                        <h1 style='color:white ;'>Mission and Vision of the Club 🎯</h1>
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
            cols1=st.columns(2)
            with cols1[0]:
                with st.expander(" 💡📜 Idea Presentation Sessions "):
                    st.markdown(""" <font color =yellow>At __Vedic Vox__</font>, we organize regular idea presentation sessions where students have the opportunity to practice articulating their thoughts and ideas. These sessions provide a supportive environment for students to share their creative concepts and receive constructive feedback from peers. By participating in these sessions, students can enhance their <font color =yellow>__public speaking skills__</font>,<font color =yellow>  __build confidence__ </font> in expressing their ideas, and refine their <font color =yellow> __presentation techniques.__</font>
                    """,unsafe_allow_html=True)
                with st.expander("🤖🧪🔭 Workshops on Entrepreneurship and Innovation"):
                    st.markdown(""" Our club hosts workshops focused on <font color= orange> entrepreneurship and innovation</font>, providing students with practical skills and knowledge to turn their ideas into reality. <font>Through interactive sessions led by ___"industry experts"___ and  ___"seasoned entrepreneurs"___, students learn about the   ___"entrepreneurial mindset"___, startup development process, </font>and strategies for <font color =orange >___Turning innovative ideas into successful ventures___</font>. These workshops not only inspire students to think creatively but also equip them with the tools and resources needed to pursue entrepreneurial endeavors""",unsafe_allow_html=True)
            with cols1[1]:
                with st.expander(" 🧑‍🏫 Guest Lectures "):
                    st.markdown('''<font>We regularly invite guest speakers from various fields, including  <font color =tangerine >__"business"__,  __"technology"__, and __"academia"__</font>, to share their insights and experiences with our members.<font color= tangerine> These guest lectures provide valuable exposure to diverse perspectives and real-world examples of successful idea implementation.</font> By attending these lectures, students gain new insights, broaden their horizons, and cultivate a deeper understanding of the    __"challenges"__ and __"opportunities"__ in their areas of interest. </font>''', unsafe_allow_html=True)
                
                with st.expander(" 🤝 📂Collaborative Projects"):
                    st.markdown('''<font color= red > __Vedic Vox__</font> facilitates collaborative projects where students can work together to explore innovative ideas and solutions to real-world problems. <font color =red>_Through teamwork and collaboration, students learn to leverage their collective strengths, brainstorm creative solutions, and execute projects effectively_</font>. These collaborative experiences not only foster critical thinking and problem-solving skills but also promote <font color= red>teamwork</font>, <font color= red>communication</font>, and <font color= red>leadership abilities</font>.''',unsafe_allow_html=True)
            
        with tab3:
            st.markdown('''
                    ## CORE MEMBERS and LEADERSHIP TEAM

                    Vedic Vox is being lead by  by <font color=#41C9E2> AMARNATH SILIVERI</font>, <font color=#41C9E2>SAI DEEKSHITHA ANDRA </font>

                    > **AMARNATH SILIVERI**: A passionate person for idea sharing with a background in Data Science and tools to get insights from data.
                        
                    > **SAI DEEKSHITHA ANDRA**: Brings expertise in organising events and sessions on idea -presentation
                        
                    

                    ### Together, they lead the club with dedication and enthusiasm.
                    ''',unsafe_allow_html=True) 
            # > **Advisor's Name**: Provides guidance based on their experience in [related field].           
if app == "Events":
    st.markdown(""" 
                    # will be disclosed soon 😁""",unsafe_allow_html=True)

if app == "Resources":
    st.markdown(""" 
                    # will be disclosed soon 😁""",unsafe_allow_html=True)

if app == "Membership":
    # Membership Benefits
        st.markdown("## Membership Benefits")
        st.write("As a member of Vedic Vox, you unlock a world of opportunities and resources to enhance your personal and professional growth. Here are some of the benefits you'll enjoy:")

        # Display Membership Perks
        st.markdown("- Access to Exclusive Events")
        st.markdown("- Workshop Discounts")
        st.markdown("- Mentorship Program")
        st.markdown("- Resource Library Access")
        st.markdown("- Networking Opportunities")
        st.markdown("- Resume Building")
        st.markdown("- Certificate of Membership")
        st.markdown("- Collaborative Projects")
        st.markdown("- Professional Development Workshops")
        st.markdown("- Leadership Opportunities")

        # Membership Registration Form
        st.markdown("## How to Join")
        st.write("To become a member of Vedic Vox, please fill out the registration form below:")

        # Display Membership Fees
        st.markdown("## Membership Fees")
        st.write("Membership fees: ₹200 per semester")

        # Submit Button
    

        with st.expander("Membership Terms and Conditions"):
                st.markdown(
                    """
                    <div>
                        <p>1. Membership Eligibility:</p>
                        <ul>
                            <li>Membership in Vedic Vox is open to all current students of [Institution Name].</li>
                            <li>Individuals must agree to abide by the club's rules and regulations.</li>
                        </ul>
                        <p>2. Membership Duration:</p>
                        <ul>
                            <li>Membership is valid for one academic semester.</li>
                            <li>Memberships may be renewed at the beginning of each semester upon payment of membership fees.</li>
                        </ul>
                        <p>3. Membership Fees:</p>
                        <ul>
                            <li>Membership fees are $50 per semester and are non-refundable.</li>
                            <li>Fees must be paid in full at the time of registration.</li>
                        </ul>
                        <p>4. Rights and Responsibilities:</p>
                        <ul>
                            <li>Members have the right to participate in all club activities and events.</li>
                            <li>Members are expected to conduct themselves in a respectful and professional manner at all times.</li>
                            <li>Members must adhere to the club's code of conduct and respect the opinions and contributions of others.</li>
                        </ul>
                        <p>5. Termination of Membership:</p>
                        <ul>
                            <li>Membership may be terminated at the discretion of the club leadership for violations of the club's rules and regulations.</li>
                            <li>Members who violate the club's code of conduct may be subject to disciplinary action, up to and including expulsion from the club.</li>
                        </ul>
                        <p>6. Privacy Policy:</p>
                        <ul>
                            <li>Vedic Vox respects the privacy of its members and will not share personal information with third parties without consent.</li>
                            <li>Members' contact information will be used solely for club-related communications and activities.</li>
                        </ul>
                        <p>7. Amendments to Terms and Conditions:</p>
                        <ul>
                            <li>These terms and conditions are subject to change at the discretion of the club leadership.</li>
                            <li>Members will be notified of any changes to the terms and conditions via email or other communication channels.</li>
                        </ul>
                        <p>By registering as a member of Vedic Vox, individuals acknowledge that they have read and understood the above terms and conditions and agree to abide by them.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                ) 

                k=st.checkbox("I agree to the terms and conditions")
                if k and st.button("JOIN THE CLUB 🚀"):
                        st.write(" ")
                        st.balloons()
                        st.markdown("# [Membership Form](https://forms.gle/mEwzZbiKX9hvy6638)")
if app == "Contact":
     

        # Define styles for the contact section
        st.markdown("""
            <style>
            .contact-section {
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #f9f9f9;
                margin-bottom: 20px;
            }

            .contact-heading {
                font-size: 24px;
                color: #333;
                margin-bottom: 10px;
            }

            .contact-info {
                font-size: 18px;
                color: #666;
                margin-bottom: 10px;
            }

            .contact-info a {
                color: #007bff;
                text-decoration: none;
            }

            .contact-info a:hover {
                text-decoration: underline;
            }
            </style>
        """, unsafe_allow_html=True)

        # Contact Us section
        st.markdown("<div class='contact-section'>", unsafe_allow_html=True)
        st.markdown("<div class='contact-heading'>Contact Us</div>", unsafe_allow_html=True)
        st.markdown("<div class='contact-info'>", unsafe_allow_html=True)
        st.markdown("- Email: <a href='mailto:VedicVox.ds@rgmcet.edu.in'>VedicVox.ds@rgmcet.edu.in</a>", unsafe_allow_html=True)
        st.markdown("- Phone (Amarnath): <a href='tel:+917207249048'>+91 7207249048</a>", unsafe_allow_html=True)
        st.markdown("- Phone (Deekshitha): <a href='tel:+919440388230'>+91 9440388230</a>", unsafe_allow_html=True)
        st.markdown("- Address: Nerawada 'X' Roads, Nandyal, Andhra Pradesh 518501", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Define styles for social icons
        st.markdown("""
            <style>
            .social-icons {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
            }

            .social-icon {
                text-align: center;
            }
            </style>
        """, unsafe_allow_html=True)

        # Social icons section
        st.markdown("<div class='social-icons'>", unsafe_allow_html=True)
        st.markdown("""
            <div class="social-icon">
                <a href="http://www.instagram.com/itz..amar." target="_blank" rel="noreferrer">
                    <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/instagram.svg" width="32" height="32" alt="Instagram" />
                </a>
                <p>Instagram</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="social-icon">
                <a href="https://chat.whatsapp.com/C7giSBe1Ex10l4wca5TMwd" target="_blank" rel="noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/128/3670/3670051.png" width="32" height="32" alt="WhatsApp" />
                </a>
                <p>WhatsApp</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="social-icon">
                <a href="mailto:VedicVox.ds@rgmcet.edu.in" target="_blank" rel="noreferrer">
                    <img src="https://cdn-icons-png.flaticon.com/128/9068/9068642.png" width="32" height="32" alt="Mail" />
                </a>
                <p>Mail</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Add Google Maps with terrain view
        st.markdown("""
            <style>
            .google-map {
                padding-bottom: 50%;
                position: relative;
            }

            .google-map iframe {
                height: 100%;
                width: 100%;
                left: 0;
                top: 0;
                position: absolute;
            }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="google-map">
                <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3844.626290194635!2d78.37430737601228!3d15.504521085096089!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bb5b49bf7e231ed%3A0xf209159e6bde969c!2sRajeev%20Gandhi%20Memorial%20College%20of%20Engineering%20and%20Technology!5e0!3m2!1sen!2sin!4v1713966806295!5m2!1sen!2sin&maptype=terrain" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
        """,unsafe_allow_html=True)

       

       
           

hide_st_style= """
       <style>
       #mainmenu {visibility:hidden;}
       footer {visibility:hidden;}
       header {visibility:hidden;}
       </style>
 """
st.markdown(hide_st_style,unsafe_allow_html=True)



     




     



      

            

          


