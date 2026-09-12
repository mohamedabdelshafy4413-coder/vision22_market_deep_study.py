import streamlit as st
import pandas as pd

st.set_page_config(page_title='Vision22 Pricing Strategy Analysis', layout='wide')

st.title('Vision22 North America Pricing & Growth Strategy')
st.subheader('USA & Canada Market Entry - Package Success Simulation')

st.markdown('''
**Positioning:** Vision22 is positioned as a B2B Growth Partner, not a low-cost digital marketing provider.
The strategy focuses on Manufacturing, B2B SaaS, Healthcare and high-value companies.
''')

packages = pd.DataFrame([
['B2B Growth Foundation',6000,9000,3000,5000,80,90],
['B2B Lead Generation Engine',8000,12000,6000,10000,90,95],
['Digital Authority & Brand Growth',12000,20000,7000,12000,75,88],
['Performance Growth System',10000,15000,8000,15000,85,92],
['Complete B2B Growth Department',20000,35000,15000,25000,65,85]
],columns=['Package','Setup Low','Setup High','Monthly Low','Monthly High','Current Success %','Best Case Success %'])

st.header('Package Analysis')
st.dataframe(packages,use_container_width=True)

st.header('Pricing Sensitivity Model')

for discount in [0,30,50]:
    st.subheader(f'Pricing Scenario: {discount}% Reduction')
    data=[]
    for _,r in packages.iterrows():
        factor=1+(discount/100)*0.15
        success=min(98,int(r['Current Success %']*factor))
        data.append([r['Package'],success])
    st.dataframe(pd.DataFrame(data,columns=['Package','Estimated Success Opportunity %']))

st.header('SWOT Analysis')
col1,col2=st.columns(2)
with col1:
 st.success('Strengths\n\n- Long marketing experience\n- Integrated services\n- Strong creative capability\n- Competitive international pricing')
 st.warning('Weaknesses\n\n- Limited US case studies\n- Need stronger local trust signals')
with col2:
 st.info('Opportunities\n\n- B2B demand generation\n- Manufacturing growth needs\n- Technology companies seeking scalable marketing')
 st.error('Threats\n\n- Strong agency competition\n- Wrong positioning as cheap provider')

st.header('Recommended Entry Strategy')
st.write('''
1. Lead with B2B Lead Generation Engine.\n
2. Use Free Growth Audit as entry offer.\n
3. Upsell Performance Growth System.\n
4. Build authority through LinkedIn content and industry reports.\n
''')

st.header('90 Day Target')
st.write('''
Goal: 3-5 clients.\n
Expected MRR after validation: $18K-$50K.\n
Focus: Quality accounts, not mass outreach.
''')
