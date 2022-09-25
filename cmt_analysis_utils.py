import pandas as pd
from lxml import etree # for reading XML files from CMT

# converts CMT xml file to a dataframe
def read_bids(filename):
    data = [] # paperID, email, bid
    doc = etree.parse(filename)
    for subm in doc.xpath('.//submission'):
        paperID = int(subm.attrib['submissionId'])
        for ch in subm.getchildren():
            bid_str = ch.attrib['bid']
            bid_id = int(bid_str.split(' ')[0])
            data.append( [paperID, ch.attrib['email'], bid_id, bid_str])
    return pd.DataFrame(data, columns=["Paper ID", "Email", "Bid_nr", "Bid"])
def read_bids_orig(filename):
    df = read_bids(filename)
    return df.rename(columns={'Paper ID': 'paperID', 'Email': 'email', 'Bid': 'bid_str', 'Bid_nr': 'bid'})

# Write out bids in CMT-compatible XML
def write_bids(df_bids, fname="Bids_cleaned.xml"):
    with open(fname, 'w') as f: # , encoding='utf-8'
        f.write("<bids>\n")
        for paperID, subdf_bids in df_bids.groupby('paperID'):
            f.write(f"  <submission submissionId=\"{paperID}\">\n")
            for row in subdf_bids[['email','bid_str']].itertuples():
                f.write(f"    <user email=\"{row.email}\" bid=\"{row.bid_str}\" />\n")
            f.write('  </submission>\n')
        f.write("</bids>\n")
        print(f"Wrote {len(df_bids)} bids to {fname}")

# converts CMT xml file to a dataframe
def read_assign(filename):
    data = [] # paperID, email
    doc = etree.parse(filename)
    for subm in doc.xpath('.//submission'):
        paperID = int(subm.attrib['submissionId'])
        for ch in subm.getchildren():
            data.append( [paperID, ch.attrib['email']])
    return pd.DataFrame(data, columns=['Paper ID', 'Email'])

# adds bidcounts to papers
def add_bidcounts_to_papers(df_papers, df_bids):
    vcnt = df_bids.groupby('Paper ID')['Bid'].value_counts()
    # add each of those as a new column with counts, so they can have value '0' too
    for bidstr in sorted(df_bids.Bid.unique()):
        df_papers[bidstr] = 0
        df_papers.loc[vcnt.loc[:,bidstr].index, bidstr] = vcnt.loc[:,bidstr]
    return df_papers


