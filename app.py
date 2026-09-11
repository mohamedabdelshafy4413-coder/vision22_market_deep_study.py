import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Vision22 North America Growth Opportunity Study", page_icon="📊", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"]{direction:rtl;text-align:right;background:#fbfdfb}
[data-testid="stSidebar"]{border-left:1px solid #d9e4dc;background:#0b0e0c}
[data-testid="stSidebar"] *{direction:rtl;text-align:right;color:#f6fff8}
.block-container{max-width:1550px;padding-top:1rem;padding-bottom:2rem}
.hero{background:linear-gradient(135deg,#080b09 0%,#111713 65%,#9ff0b2 170%);border:1px solid #27352b;border-radius:24px;padding:28px 30px;margin-bottom:18px;box-shadow:0 14px 40px rgba(0,0,0,.12)}
.hero h1{color:#fff;margin:8px 0 0;font-size:2.15rem}.hero p{color:#dce8df;line-height:1.8;margin:.65rem 0 0}
.tag{display:inline-block;background:#c9ffd5;color:#07150b;border-radius:999px;padding:5px 11px;margin-left:6px;font-size:.76rem;font-weight:800}
.kpi{background:#fff;border:1px solid #dce7df;border-radius:16px;padding:16px 18px;min-height:126px;box-shadow:0 6px 18px rgba(10,30,18,.05)}
.kpi .label{font-size:.82rem;color:#58675e}.kpi .value{font-size:1.47rem;font-weight:850;color:#0c1710;margin:.3rem 0}.kpi .note{font-size:.78rem;color:#6b786f;line-height:1.5}
.panel{background:#fff;border:1px solid #dce7df;border-radius:16px;padding:18px 20px;margin:.55rem 0 1rem}.good{border-right:5px solid #61d881;background:#f3fff6}.warn{border-right:5px solid #e5b34f;background:#fffaf0}.risk{border-right:5px solid #db6a6a;background:#fff5f5}
.small{font-size:.82rem;color:#657169}
</style>
""", unsafe_allow_html=True)

market_evidence = pd.DataFrame([
    ["USA digital ad revenue — 2025", "$294.6B", "+13.9% YoY", "IAB / PwC 2026", "Market Evidence"],
    ["Canada digital ad revenue — 2025", "$21.1B", "+16% YoY", "IAB Canada 2026", "Market Evidence"],
    ["US Search share of digital ad revenue", "38.8%", "+11.0% YoY", "IAB / PwC 2026", "Market Evidence"],
    ["US Digital Video growth", "25.4%", "YoY", "IAB / PwC 2026", "Market Evidence"],
    ["Canada Video growth", "26%", "YoY", "IAB Canada 2026", "Market Evidence"],
    ["B2B marketers increasing lead-gen budgets", "~70%", "Top investment area", "LinkedIn B2B Benchmark", "Market Evidence"],
    ["B2B marketers lacking efficient lead-gen/nurture", "47%", "Capability gap", "Content Marketing Institute", "Market Evidence"],
    ["B2B buyers preferring rep-free experience", "67%", "Buyer behavior", "Gartner 2026", "Market Evidence"],
    ["B2B buyers avoiding irrelevant outreach", "73%", "Outreach risk", "Gartner 2025", "Market Evidence"],
], columns=["المؤشر","القيمة","الدلالة","المصدر","النوع"])

industries = pd.DataFrame([
    ["Industrial & Manufacturing",94,"$8K–$30K/mo","CEO / VP Sales / Marketing Director","Lead pipeline, SEO visibility, buyer acquisition","Texas, Illinois, Ohio, Ontario","Wave 1"],
    ["Construction & Engineering",90,"$7K–$25K/mo","CEO / BD Director / Marketing Director","Project pipeline, search demand, proof","Texas, Florida, North Carolina, Alberta","Wave 1"],
    ["B2B SaaS & Technology",88,"$10K–$40K/mo","Founder / CMO / VP Growth / VP Sales","Demand generation, CAC pressure, pipeline quality","California, Texas, North Carolina, Ontario, BC","Wave 1"],
    ["Industrial Distribution & Wholesale",87,"$8K–$25K/mo","President / VP Sales / BD","New accounts, dealer demand, weak digital acquisition","Illinois, Texas, Ohio, Ontario","Wave 1"],
    ["Logistics & 3PL",83,"$7K–$20K/mo","CEO / VP Sales / Commercial Director","Qualified shipper accounts, account growth","Texas, Illinois, Ontario, BC","Wave 2"],
    ["Packaging & Materials",82,"$8K–$22K/mo","CEO / Sales Director / Marketing","Long-cycle acquisition, RFQ generation","Illinois, Ohio, Ontario","Wave 2"],
    ["Energy & Industrial Services",81,"$10K–$30K/mo","Commercial Director / BD / CEO","High-value contracts, account targeting, authority","Texas, Alberta","Wave 2"],
    ["Specialty Equipment & Commercial Services",80,"$7K–$20K/mo","President / Sales Director","High-ticket lead generation and conversion","Texas, Ohio, Ontario, Alberta","Wave 2"],
    ["Professional B2B Services",77,"$5K–$15K/mo","Managing Partner / Marketing Director","Authority, inbound leads, differentiation","Florida, Texas, Ontario","Wave 2"],
    ["Commercial Real Estate Services",75,"$6K–$18K/mo","Principal / BD / Marketing","Deal flow, local demand, authority","Florida, Texas, Ontario","Wave 3"],
], columns=["Industry","Vision22 Entry Score","Proposed Offer Range","Decision Makers","Core Need","Priority Geography","Wave"])

geo = pd.DataFrame([
    ["USA","Texas",96,"Manufacturing, construction, energy, B2B services","ابدأ فورًا"],
    ["Canada","Ontario",94,"Manufacturing, SaaS, distribution, services","أولوية كندا"],
    ["USA","Illinois",91,"Industrial, distribution, logistics, manufacturing","ابدأ فورًا"],
    ["Canada","Alberta",89,"Energy, engineering, construction, industrial services","أولوية كندا"],
    ["USA","North Carolina",88,"Advanced manufacturing, SaaS, services","ابدأ فورًا"],
    ["USA","Ohio",87,"Manufacturing, industrial suppliers, equipment","Cluster ثانٍ"],
    ["USA","Florida",84,"Construction, services, commercial real estate","Cluster ثانٍ"],
    ["Canada","British Columbia",82,"Technology, logistics, professional services","انتقائي"],
    ["USA","California",82,"SaaS, technology, advanced manufacturing","انتقائي بسبب المنافسة"],
    ["Canada","Quebec",76,"Manufacturing, tech, industrial","يحتاج French localization"],
], columns=["Country","Market","Strategic Score","Best-fit Sectors","Entry Note"])

packages = pd.DataFrame([
    ["Lead Generation Engine",92,96,90,82,"$7K–$20K/mo","Monthly","Fastest","أفضل عرض دخول"],
    ["Website & Conversion System",86,93,84,80,"$10K–$50K/project","Project","Fast-Medium","ألم واضح ويمكن إثباته بالـAudit"],
    ["Performance Growth System",84,91,78,90,"$8K–$30K/mo","Monthly","Medium","قيمة عالية ويحتاج Attribution قوي"],
    ["Growth Foundation",80,87,88,60,"$5K–$10K/project","Project","Fast","Entry product منخفض الاحتكاك"],
    ["Digital Authority System",76,82,72,76,"$5K–$20K/mo","Monthly","Medium","يبني الثقة على مدى أطول"],
    ["Complete B2B Marketing Department",72,85,52,100,"$15K–$50K/mo","Monthly","Slow","أعلى قيمة وأعلى حاجز ثقة"],
    ["International B2B Expansion",68,70,60,88,"$10K–$35K/project","Project","Medium-Slow","مناسب للمصنعين والمصدرين"],
], columns=["Package","90-Day Sales Score","Market Opportunity","Ease of Close","Price Power","Pricing","Model","Sales Velocity","Strategic Note"])

package_details = {
"Lead Generation Engine":("Manufacturing, construction, distribution, B2B SaaS",["ICP Research","Target Account Strategy","Google Ads","LinkedIn Ads","Landing Pages","Lead Forms","Conversion Tracking","Email Nurturing","Monthly Optimization"],"Qualified leads, meetings, CPL, opportunity value, pipeline"),
"Website & Conversion System":("Companies with weak site/message/conversion",["Messaging Strategy","Buyer Journey","UX/UI","Website Development","Landing Pages","CTA Strategy","Lead Capture","Case Studies","Sales Materials"],"Conversion rate, RFQs, demos, qualified inquiries"),
"Performance Growth System":("Companies already investing in acquisition",["Google Ads","LinkedIn Ads","Remarketing","Creative Testing","A/B Testing","Landing Optimization","Attribution Review","ROI Reporting"],"CAC/CPL, pipeline, conversion rate, channel ROI"),
"Growth Foundation":("Under-structured marketing teams",["Market Research","Competitor Analysis","ICP","Buyer Persona","Digital Audit","SEO Audit","Conversion Audit","90-Day Roadmap"],"Prioritized backlog, channel plan, upsell conversion"),
"Digital Authority System":("Complex B2B with long sales cycles",["Technical SEO","Keyword Strategy","Industry Content","Case Studies","White Papers","LinkedIn Content","Executive Thought Leadership","Digital PR"],"Organic visibility, inbound opportunities, assisted pipeline"),
"Complete B2B Marketing Department":("Mid-market firms outsourcing marketing",["Growth Strategy","Paid Media","SEO","Content","Social","Creative","Website Optimization","Email","Sales Enablement","Reporting"],"Pipeline, revenue influence, ROI, MQL-to-SQL, retention"),
"International B2B Expansion":("Manufacturers, exporters, suppliers",["Country Analysis","Competitor Mapping","Buyer Identification","Decision-Maker Research","Prospect Database","Outreach Strategy","Sales Materials","Market Entry Roadmap"],"Qualified accounts, RFQs, distributor meetings, pipeline by geography")
}

emails = [
("01 — Pipeline Gap","CEO / VP Sales — Manufacturing & Distribution","A quick pipeline observation for [Company Name]","Hello [First Name],\n\nI reviewed [Company Name] and noticed a few opportunities to strengthen how your digital presence converts market interest into qualified sales conversations.\n\nVision22 works with B2B companies across strategy, lead generation, paid acquisition, SEO and conversion improvement. Rather than suggest a generic campaign, I can send you a short 3-point growth review focused specifically on [Company Name].\n\nWould it be useful if I sent that over?\n\nBest regards,\nVision22"),
("02 — Manufacturing Growth","President / Sales Director — Manufacturing","Potential B2B growth opportunities for [Company Name]","Hello [First Name],\n\nCompanies in industrial markets often have strong products and sales teams but limited digital systems for consistently creating qualified opportunities.\n\nAfter reviewing [Company Name], I identified several areas worth testing across search visibility, targeted acquisition and conversion.\n\nIf helpful, we can prepare a concise 90-day opportunity map showing where Vision22 would focus first and what we would measure.\n\nWould a short review next week be relevant?\n\nBest regards,\nVision22"),
("03 — Website Conversion","Marketing Director / CEO","One conversion opportunity on [Company Name]’s website","Hello [First Name],\n\nI spent a few minutes reviewing [Company Name]’s digital journey. There appears to be an opportunity to make the website work harder as a B2B sales asset — particularly around messaging, proof and lead capture.\n\nVision22 combines website conversion strategy with acquisition and content, so the goal is not a redesign for its own sake; it is more qualified inquiries.\n\nI can send a brief conversion review with the first issues we would prioritize. Interested?\n\nBest regards,\nVision22"),
("04 — Competitive Gap","CEO / Marketing Director","A digital gap we noticed versus your market","Hello [First Name],\n\nWhile reviewing [Company Name] and several competitors in your category, we noticed a gap in how companies are competing for high-intent B2B demand online.\n\nThere may be room for [Company Name] to improve visibility and capture more qualified opportunities without broad, unfocused marketing.\n\nVision22 can summarize the opportunity in a short competitor and demand review.\n\nWould you like me to send it?\n\nBest regards,\nVision22"),
("05 — 90-Day Plan","Founder / CEO / VP Sales","90-day B2B growth plan for [Company Name]","Hello [First Name],\n\nI’m reaching out with a specific idea rather than a general agency introduction.\n\nFor [Company Name], I would structure the first 90 days around three priorities: target-account clarity, qualified demand generation, and stronger conversion from digital touchpoints.\n\nVision22 can prepare the initial plan before discussing a larger engagement, so you can judge the thinking first.\n\nWould a 15-minute conversation be worthwhile?\n\nBest regards,\nVision22"),
("06 — SaaS Demand","Founder / CMO / VP Growth — B2B SaaS","Improving qualified demand for [Company Name]","Hello [First Name],\n\nI reviewed [Company Name] from a B2B acquisition perspective. The opportunity I see is less about generating more traffic and more about creating qualified demand that can progress into pipeline.\n\nVision22’s approach combines positioning, paid acquisition, conversion and content around the same ICP and revenue objective.\n\nIf you are reviewing pipeline efficiency this quarter, I can share a short diagnostic with the first tests we would run. Open to that?\n\nBest regards,\nVision22"),
("07 — Construction Pipeline","CEO / BD Director — Construction & Engineering","A project-pipeline idea for [Company Name]","Hello [First Name],\n\nFor engineering and construction firms, digital marketing only matters when it supports real project opportunities and credibility with decision-makers.\n\nI reviewed [Company Name] and see potential to strengthen both high-intent discovery and the proof buyers see before making contact.\n\nVision22 can outline a focused lead-generation and conversion plan rather than a broad marketing package.\n\nShould I send the short version?\n\nBest regards,\nVision22"),
("08 — Authority & SEO","Marketing Director / Managing Partner","Search visibility opportunity for [Company Name]","Hello [First Name],\n\nYour buyers increasingly research suppliers independently before speaking with sales. That makes search visibility, proof and expert content commercially important — especially in longer B2B buying cycles.\n\nWe noticed a few areas where [Company Name] could strengthen digital authority around high-value topics and buying intent.\n\nI can send a concise visibility review with the priority opportunities. Would that be useful?\n\nBest regards,\nVision22"),
("09 — Outsourced Department","CEO / COO — Mid-market","An alternative to expanding your internal marketing team","Hello [First Name],\n\nIf [Company Name] is planning to increase marketing output without building a large internal team, there may be a practical alternative.\n\nVision22 can operate as an integrated B2B marketing partner across strategy, paid acquisition, SEO, content, conversion and reporting — with one commercial plan and one accountable team.\n\nI’d be happy to outline what an outsourced model could look like for your current stage.\n\nWould a brief discussion make sense?\n\nBest regards,\nVision22"),
("10 — International Expansion","CEO / Export Director / BD","North American buyer development for [Company Name]","Hello [First Name],\n\nI’m contacting you regarding a possible market-development opportunity for [Company Name].\n\nFor B2B manufacturers and suppliers, Vision22 can support expansion through market prioritization, buyer mapping, decision-maker research, digital positioning and targeted demand generation.\n\nThe first step would be a focused market-entry assessment rather than a broad campaign.\n\nIf North American growth is on your agenda, would you be open to receiving a short outline?\n\nBest regards,\nVision22")
]

risks = pd.DataFrame([
    ["No North American proof",5,5,25,"3 quantified case studies + pilot offer + senior strategy lead"],
    ["Generic outbound messaging",5,4,20,"Segment by industry, trigger and role; personalize first lines"],
    ["CASL non-compliance in Canada",5,4,20,"Consent basis + identification + unsubscribe + evidence records"],
    ["Poor email deliverability",4,4,16,"Separate domains, SPF/DKIM/DMARC, verification, controlled volumes"],
    ["Long B2B sales cycles",4,4,16,"Diagnostic entry offer, nurture, proof assets, multi-threading"],
    ["Overpromising revenue",4,4,16,"Sell process and pipeline KPIs; avoid unsupported guarantees"],
    ["Delivery capacity constraints",4,3,12,"Capacity model, onboarding limits, QA, standard reporting"],
    ["High competition",3,4,12,"Vertical proof, selective geographies, do not compete on price"],
    ["Cross-border contracting/payment",3,3,9,"USD terms, clear SOW, payment policy, legal/tax review"],
    ["Weak sales follow-up",4,4,16,"CRM stages, owner, next step, weekly pipeline review"]
], columns=["Risk","Impact","Likelihood","Risk Score","Mitigation"])

sources = pd.DataFrame([
    ["IAB / PwC — Internet Advertising Revenue Report 2025","https://www.iab.com/insights/internet-advertising-revenue-report-full-year-2025/"],
    ["IAB Canada — Digital Advertising Market 2025","https://iabcanada.com/canadas-digital-advertising-market-shows-strong-growth-in-2025/"],
    ["LinkedIn — B2B Lead Generation","https://www.linkedin.com/business/marketing/blog/content-marketing/what-is-lead-generation"],
    ["Content Marketing Institute — B2B 2025","https://contentmarketinginstitute.com/b2b-research/b2b-content-marketing-trends-research-2025"],
    ["Gartner — B2B Buyer Survey 2026","https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience"],
    ["Gartner — B2B Buyer Survey 2025","https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience"],
    ["CRTC — CASL Guidance","https://crtc.gc.ca/eng/com500/guide.htm"],
    ["FTC — CAN-SPAM Act","https://www.ftc.gov/legal-library/browse/statutes/controlling-assault-non-solicited-pornography-marketing-act-2003-can-spam-act"]
], columns=["Source","URL"])

st.markdown("""
<div class="hero"><span class="tag">VISION22</span><span class="tag">USA + CANADA</span><span class="tag">B2B</span>
<h1>دراسة فرص النمو والتوسع لـ Vision22 في أمريكا وكندا</h1>
<p>Dashboard تحليلية تفصيلية لدخول السوق، اختيار القطاعات، هندسة الباقات، البريد البيعي، التوقع المالي، SWOT والمخاطر. يتم الفصل بوضوح بين Market Evidence المنشور وبين Vision22 Strategic Estimates.</p></div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## Vision22 Study")
    section = st.radio("انتقل إلى", ["الخلاصة التنفيذية","إحصائيات السوق","أقوى نقطة دخول","القطاعات المستهدفة","المناطق الجغرافية","ICP & Buying Committee","الباقات والخدمات","ترتيب فرص الباقات","Email Campaigns","خطة 90 يوم","التوقعات المالية","SWOT Analysis","المخاطر والحلول","متطلبات الإطلاق","المصادر والمنهجية"])
    st.divider(); st.caption("Market snapshot: September 2026"); st.caption("Strategic Scores = تقديرات تخطيطية داخلية وليست ضمانات.")

if section == "الخلاصة التنفيذية":
    c1,c2,c3,c4=st.columns(4)
    for c,label,value,note in [(c1,"أقوى عرض للدخول","Lead Generation Engine","أوضح ROI وأسرع conversation"),(c2,"أولوية القطاعات","Industrial B2B","Manufacturing + Construction + Distribution"),(c3,"نطاق العقود","$7K–$50K","حسب Scope ونوع العقد"),(c4,"التسلسل الجغرافي","USA → Canada","70% USA / 30% Canada كبداية")]:
        with c: st.markdown(f'<div class="kpi"><div class="label">{label}</div><div class="value">{value}</div><div class="note">{note}</div></div>',unsafe_allow_html=True)
    st.markdown('<div class="panel good"><b>الخلاصة:</b> لا ندخل كـ general digital agency. ندخل كـ B2B growth partner لقطاعات ذات قيمة صفقة مرتفعة. نكسب الحساب بمشكلة Pipeline محددة، ثم نوسع الخدمات داخل الحساب.</div>',unsafe_allow_html=True)
    st.write("**Phase 1:** Texas + Illinois + North Carolina، مع Ontario وAlberta انتقائيًا. **Verticals:** Industrial & Manufacturing، Construction & Engineering، Industrial Distribution، ثم B2B SaaS. **Commercial wedge:** audit مخصص → discovery → 90-day pilot/setup → retainer.")
    st.subheader("أرقام السوق التي تدعم القرار"); st.dataframe(market_evidence.head(7),use_container_width=True,hide_index=True)

elif section == "إحصائيات السوق":
    st.header("إحصائيات السوق — Market Evidence"); st.info("الأرقام التالية منشورة من مصادر خارجية وليست تقديرات Vision22."); st.dataframe(market_evidence,use_container_width=True,hide_index=True)
    a,b,c=st.columns(3); a.metric("USA Digital Ads 2025","$294.6B","+13.9%"); b.metric("Canada Digital Ads 2025","$21.1B","+16%"); c.metric("Lead-gen budget increase","~70%","B2B marketers")
    st.write("**الاستنتاج:** السوق لا يحتاج إثبات أن Digital مهم؛ Vision22 تحتاج إثبات الأثر التجاري. Search مهم للطلب عالي النية، والفيديو يدعم Performance كطبقة Creative، وفجوة lead-gen/nurturing تدعم جعل Lead Generation Engine رأس الحربة.")

elif section == "أقوى نقطة دخول":
    st.header("أقوى نقطة دخول للسوق"); st.markdown('<div class="panel good"><b>الأولوية #1:</b> Lead Generation Engine لقطاعات Industrial & Manufacturing / Construction / Distribution في USA، ثم Website & Conversion وPerformance كـ upsell.</div>',unsafe_allow_html=True)
    st.write("**لماذا؟** المشكلة مفهومة لدى CEO وVP Sales، ويمكن قياسها بالـpipeline، وقيمة الصفقة في القطاعات المستهدفة تجعل Retainer عاليًا قابلًا للدفاع عنه، والعرض يفتح upsell واسع.")
    st.subheader("USA أولًا، Canada ثانيًا"); st.write("**USA:** outbound أسرع مع التزام CAN-SPAM. **Canada:** CASL أكثر صرامة؛ نرفع وزن LinkedIn، referrals، partnerships والحسابات التي يتوفر لها consent basis صالح.")
    entry=pd.DataFrame([[1,"Vertical Selection","3 verticals فقط","وضوح message-market fit"],[2,"Account Qualification","High-value accounts","تركيز المجهود"],[3,"Diagnostic Hook","3-point audit","قيمة قبل البيع"],[4,"Pilot / Setup","90-day scoped engagement","تقليل حاجز الثقة"],[5,"Retainer Expansion","Performance / Authority / Full Department","رفع LTV"]],columns=["Step","Action","Execution","Why"]); st.dataframe(entry,use_container_width=True,hide_index=True)

elif section == "القطاعات المستهدفة":
    st.header("القطاعات المستهدفة وترتيبها"); st.caption("Vision22 Entry Score = Strategic Estimate داخلي."); view=industries.sort_values("Vision22 Entry Score",ascending=False); st.dataframe(view,use_container_width=True,hide_index=True); st.plotly_chart(px.bar(view,x="Industry",y="Vision22 Entry Score",text="Vision22 Entry Score"),use_container_width=True)
    for ind in ["Industrial & Manufacturing","Construction & Engineering","B2B SaaS & Technology","Industrial Distribution & Wholesale"]:
        r=industries[industries["Industry"]==ind].iloc[0]
        with st.expander(ind,expanded=ind=="Industrial & Manufacturing"):
            st.write(f"**Score:** {r['Vision22 Entry Score']}/100 | **Offer:** {r['Proposed Offer Range']} | **Decision Makers:** {r['Decision Makers']}"); st.write(f"**Core Need:** {r['Core Need']} | **Geography:** {r['Priority Geography']}"); st.write("**Sales angle:** لا نبيع social media management؛ نبدأ من pipeline / RFQ / demo / qualified opportunity.")

elif section == "المناطق الجغرافية":
    st.header("أين نبدأ؟"); st.caption("Strategic Score = ترتيب داخلي."); st.dataframe(geo.sort_values("Strategic Score",ascending=False),use_container_width=True,hide_index=True); st.plotly_chart(px.bar(geo.sort_values("Strategic Score"),x="Strategic Score",y="Market",color="Country",orientation="h"),use_container_width=True); st.write("**Wave 1 USA:** Texas → Illinois → North Carolina. **Wave 1 Canada:** Ontario → Alberta. California انتقائي بسبب المنافسة، وQuebec بعد تجهيز French localization.")

elif section == "ICP & Buying Committee":
    st.header("ICP & Buying Committee"); st.write("**Ideal Company:** B2B، غالبًا 20–500 موظف كبداية، قيمة صفقة مرتفعة، فريق Sales قادر على follow-up، قدرة تشغيلية لاستيعاب demand، وإما Marketing spend قائم أو gap رقمي واضح.")
    committee=pd.DataFrame([["CEO / President","Revenue, expansion, risk","Pipeline value + accountability"],["VP Sales / Sales Director","Qualified opportunities","SQL quality + meetings + pipeline"],["CMO / Marketing Director","Channel performance","CAC/CPL + conversion + reporting"],["Business Development Director","New accounts / territories","Target accounts + RFQs + meetings"],["COO / CFO","Cost and risk","ROI logic + contract terms"]],columns=["Role","Primary Concern","What Vision22 Must Prove"]); st.dataframe(committee,use_container_width=True,hide_index=True); st.warning("في العقود الكبيرة لا نعتمد على Contact واحد؛ نعمل multi-thread مع 2–4 أطراف من لجنة الشراء.")

elif section == "الباقات والخدمات":
    st.header("الباقات والخدمات"); st.caption("الأسعار Vision22 proposed ranges وليست market averages رسمية.")
    for _,r in packages.iterrows():
        fit,services,kpis=package_details[r['Package']]
        with st.expander(f"{r['Package']} — {r['Pricing']}",expanded=r['Package']=="Lead Generation Engine"):
            a,b,c,d=st.columns(4); a.metric("90-Day Sales",f"{r['90-Day Sales Score']}/100"); b.metric("Opportunity",f"{r['Market Opportunity']}/100"); c.metric("Ease of Close",f"{r['Ease of Close']}/100"); d.metric("Price Power",f"{r['Price Power']}/100"); st.write(f"**Best Fit:** {fit}"); st.write("**Included:** "+" • ".join(services)); st.write(f"**KPIs:** {kpis}"); st.write(f"**Velocity:** {r['Sales Velocity']} | **Model:** {r['Model']} | **Note:** {r['Strategic Note']}")

elif section == "ترتيب فرص الباقات":
    st.header("ترتيب الباقات لأول 90 يوم"); ranked=packages.sort_values("90-Day Sales Score",ascending=False); st.dataframe(ranked,use_container_width=True,hide_index=True); st.plotly_chart(px.bar(ranked,x="Package",y=["90-Day Sales Score","Market Opportunity","Price Power"],barmode="group"),use_container_width=True); st.write("**Lead Generation Engine** أفضل توازن. **Website & Conversion** ممتاز كـ audit-led sale. **Performance Growth** قيمته عالية لكن يحتاج proof. **Complete B2B Marketing Department** الأغلى والأعلى LTV لكنه ليس العرض الأول في cold outreach.")

elif section == "Email Campaigns":
    st.header("10 Email Campaigns احترافية"); st.warning("73% من B2B buyers في Gartner 2025 يتجنبون الموردين الذين يرسلون outreach غير ذي صلة؛ التخصيص جزء أساسي من الاستراتيجية.")
    for i,(name,target,subject,body) in enumerate(emails):
        with st.expander(name,expanded=i==0): st.write(f"**Target:** {target}"); st.write(f"**Subject:** {subject}"); st.code(body,language=None)
    st.subheader("Sequence"); st.write("Day 1: personalized insight • Day 4: proof/observation • Day 9: mini case/competitor gap • Day 16: close-the-loop. USA: CAN-SPAM compliance. Canada: CASL consent basis + identification + unsubscribe + records.")

elif section == "خطة 90 يوم":
    st.header("خطة دخول 90 يوم"); plan=pd.DataFrame([["Days 1–15","Foundation","3 verticals + geographies + packages + 3 case studies + compliance + infrastructure","Readiness ≥85/100"],["Days 16–30","List + Messaging","1,000–1,500 qualified USA accounts + compliant Canada segment + audits","Valid contacts + segmentation"],["Days 31–45","Pilot Outreach","Small cohorts + 2–3 angles per vertical + manual reply review","Positive reply + meeting quality"],["Days 46–60","Proof Loop","Objection learning + proof assets + retargeting + multi-threading","Proposal quality"],["Days 61–75","Scale Winners","Scale only winning segments + second cluster","Pipeline coverage"],["Days 76–90","Close + Expand","Close retainers + upsell + referral loop + new case studies","Exit MRR + pipeline"]],columns=["Period","Phase","Actions","Primary KPI"]); st.dataframe(plan,use_container_width=True,hide_index=True)
    mix=pd.DataFrame([["Targeted Email / Direct Outreach",35],["LinkedIn & Executive Outreach",25],["SEO / High-intent Content",15],["Google Search / Paid Demand",15],["Partnerships / Referrals",10]],columns=["Channel","Initial Focus %"]); st.plotly_chart(px.pie(mix,values="Initial Focus %",names="Channel",hole=.48),use_container_width=True); st.caption("Channel mix = Vision22 planning assumption; يُعدل بعد بيانات أول 30 يوم.")

elif section == "التوقعات المالية":
    st.header("التوقعات المالية لأول 90 يوم"); st.warning("Scenario Model وليست ضمانًا."); scenarios=pd.DataFrame([["Conservative",2,9000,18000,"Proof building أبطأ"],["Base / Target",5,12000,60000,"Focused execution"],["Strong Execution",9,15000,135000,"Strong proof + sales discipline"]],columns=["Scenario","Clients Won","Avg Monthly Retainer","Exit MRR","Interpretation"]); st.dataframe(scenarios,use_container_width=True,hide_index=True); st.plotly_chart(px.bar(scenarios,x="Scenario",y="Exit MRR",text="Exit MRR"),use_container_width=True)
    a,b,c,d=st.columns(4); accounts=a.number_input("Qualified accounts contacted",100,20000,3000,100); positive=b.slider("Positive response %",0.2,8.0,1.8,0.1); meeting=c.slider("Response → meeting %",10,80,40); close=d.slider("Meeting → client %",5,50,18); retainer=st.slider("Average monthly retainer ($)",5000,50000,12000,1000); responses=accounts*positive/100; meetings=responses*meeting/100; clients=meetings*close/100; mrr=clients*retainer; x1,x2,x3,x4=st.columns(4); x1.metric("Responses",f"{responses:.1f}"); x2.metric("Meetings",f"{meetings:.1f}"); x3.metric("Wins",f"{clients:.1f}"); x4.metric("Modelled Exit MRR",f"${mrr:,.0f}"); st.caption("Conversion defaults are internal planning assumptions; replace with actual data after first 500–1,000 qualified accounts.")

elif section == "SWOT Analysis":
    st.header("SWOT Analysis كاملة"); a,b=st.columns(2)
    with a:
        st.subheader("Strengths"); st.write("✅ Integrated strategy + creative + paid + SEO + conversion\n\n✅ One accountable team\n\n✅ Strong value structure without low-cost positioning\n\n✅ Ability to turn regional experience into quantified proof")
        st.subheader("Opportunities"); st.write("📈 Lead generation is a major B2B budget priority\n\n📈 47% report lead-gen/nurturing gaps\n\n📈 USA and Canada digital ad markets continue growing\n\n📈 Industrial sectors often have high deal values and digital gaps")
    with b:
        st.subheader("Weaknesses"); st.write("⚠️ Limited North American recognition\n\n⚠️ Limited local testimonials initially\n\n⚠️ Time-zone and communication discipline required\n\n⚠️ Broad capability can look generic without vertical positioning")
        st.subheader("Threats"); st.write("🛑 Crowded agency market\n\n🛑 73% avoid irrelevant outreach\n\n🛑 CASL constraints in Canada\n\n🛑 Economic volatility can raise ROI scrutiny")
    st.success("الاستنتاج: التموضع التسويقي ضيق، لكن delivery capability واسعة. نكسب الحساب برسالة pipeline/conversion ثم نوسع الخدمات داخله.")

elif section == "المخاطر والحلول":
    st.header("Risk Register"); st.caption("Risk Score = Impact × Likelihood كتقييم تخطيطي داخلي."); rr=risks.sort_values("Risk Score",ascending=False); st.dataframe(rr,use_container_width=True,hide_index=True); st.plotly_chart(px.bar(rr,x="Risk",y="Risk Score"),use_container_width=True); st.write("**أعلى المخاطر:** proof ضعيف، outreach عام، وتطبيق outbound أمريكي على كندا بدون CASL.")

elif section == "متطلبات الإطلاق":
    st.header("ما المطلوب قبل أول Campaign؟"); readiness=pd.DataFrame([["Positioning","3 vertical value propositions","Critical"],["Proof","3 quantified case studies + one-page versions","Critical"],["Website","North America landing page + package pages + calendar","Critical"],["Sales Assets","Agency deck + audit + proposal/SOW","Critical"],["Email Infrastructure","Separate domains + SPF/DKIM/DMARC + verification","Critical"],["Compliance","CAN-SPAM checklist + CASL consent process","Critical"],["CRM","Stages + owner + next step + loss reason","High"],["Reporting","Pipeline + qualified lead dashboard","High"],["Delivery","Capacity per package + onboarding + QA","High"],["Commercial","USD pricing + scope + payment/cancellation terms","High"],["Local Trust","Time-zone coverage + testimonials/partners","Medium-High"],["Content","Vertical case studies + insight content","Medium"]],columns=["Area","Required Asset / Process","Priority"]); st.dataframe(readiness,use_container_width=True,hide_index=True); st.success("Launch Gate: لا نعمل scale قبل اكتمال كل عناصر Critical.")

else:
    st.header("المصادر والمنهجية"); st.write("**Market Evidence** = أرقام منشورة كما كانت متاحة في سبتمبر 2026. **Vision22 Strategic Estimate** = درجات الأولوية والأسعار والسيناريوهات هي أدوات تخطيط وليست benchmarks رسمية أو ضمانات."); st.dataframe(sources,use_container_width=True,hide_index=True); st.write("**USA / CAN-SPAM:** التزم بالهوية والعنوان والـopt-out وعدم التضليل. **Canada / CASL:** يلزم consent مناسب، identification وunsubscribe، مع الاحتفاظ بإثبات الأساس القانوني للإرسال. هذه الدراسة ليست استشارة قانونية.")

st.divider(); st.caption("Vision22 North America Growth Opportunity Study • Market snapshot: September 2026 • Light green / black / white")