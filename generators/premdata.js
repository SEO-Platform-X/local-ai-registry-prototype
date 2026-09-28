    const TY = [['ds', 'Directory submissions', '#7b4fd6', 1],
      ['rd', 'Negative review disputes', '#c13515', 2], ['rr', 'Review replies, autopilot', '#237233', 2], ['qa', 'Answers to locals, autopilot', '#e8a000', 2], ['pr', 'Press releases', '#13203a', 2], ['mc', 'AI code on photos', '#0f9d8f', 2], ['gp', 'Google posts', '#2d6fd6', 2], ['go', 'Google profile optimization', '#5b8def', 2], ['rl', 'Review link', '#8fbf6a', 2], ['rv', 'Review velocity check', '#b3a14a', 2],
      ['tf', 'Technical fixes', '#6a6a6a', 3], ['sp', 'Speed optimization', '#9a9a9a', 3], ['ur', 'URL restructuring', '#4a5466', 3], ['tm', 'Topical map', '#8a5a2b', 3], ['sc', 'Semantic content', '#b8460a', 3], ['cn', 'Cannibalization fix', '#a32222', 3], ['em', 'Entity mapping', '#4a2a91', 3], ['ar', 'Articles', '#e0457b', 3], ['bl', 'Blogs', '#f08a5d', 3], ['nb', 'Only, first and best story', '#222222', 3]];
    const TC = {}; TY.forEach(x => TC[x[0]] = x);
    const IT = [];
    const add = (d, k, t, dest, body, img) => IT.push({ d, k, t, dest, body, img: img || '' });
    const DIRS = ['Apple Maps', 'Bing Places', 'Yelp', 'Healthgrades', 'Zocdoc', 'RealSelf', 'Nextdoor', 'Foursquare', 'Yellow Pages', 'Manta', 'BBB', 'Chamber of Commerce', 'Superpages', 'Citysearch', 'Hotfrog', 'MapQuest', 'Brownbook', 'Cylex', 'Tupalo', 'EZlocal', 'Local.com', 'Merchant Circle', 'Show Me Local', 'Judy\u2019s Book', 'Yellowbot', 'Opendi', 'Find Open', 'iBegin', 'n49', 'Spoke', 'Storeboard'];
    for (let d = 1; d <= 31; d++) add(d, 'ds', 'Submit to ' + DIRS[d - 1], DIRS[d - 1], 'Lumen Aesthetics, 9891 Irvine Center Dr, Suite 210, Irvine, CA 92618. (949) 555-0148. Doctor-led med spa: lip filler, Botox, Morpheus8. HSA accepted.');
    [2, 9, 16, 23, 30].forEach((d, i) => add(d, 'rd', 'Dispute a ' + ['1-star Google review', '2-star Yelp review', '1-star Google review', 'fake Yelp review', '1-star RealSelf review'][i], ['Google', 'Yelp', 'Google', 'Yelp', 'RealSelf'][i], 'The reviewer was never a patient. We ask the platform to remove it under its conflict of interest policy.'));
    [5, 7, 12, 14, 19, 21, 26, 28].forEach(d => add(d, 'rr', 'Autopilot replies to new reviews', 'Google, Yelp, RealSelf', 'Thank you! Dr. Nair loved seeing your results. See you in the spring.\n\nPriya and the Lumen team'));
    [6, 13, 20, 27].forEach(d => add(d, 'qa', 'Autopilot answers to new questions', 'Your page, under Locals', 'Yes, HSA and FSA cards are accepted for most treatments. Bring your card to your consult.'));
    add(15, 'pr', 'Press release: Skin Night', 'Wire and 30 outlets', 'IRVINE, Calif. Lumen Aesthetics invites the community to Skin Night on October 15, with live Morpheus8 demos by Dr. Priya Nair.', 'Press photo of Dr. Nair');
    add(8, 'mc', 'AI code on 51 photos', 'Your page and website', 'Adds what, where and who to every photo, in the format AI reads.', 'Treatment room');
    [6, 13, 20, 27].forEach((d, i) => add(d, 'gp', ['Morpheus8 Body is here', 'Meet our nurse injectors', 'Skin Night is next week', 'Fall skin prep'][i], 'Google Business Profile', 'Morpheus8 Body is here. Arms, stomach and knees. Consults start October 1 with Dr. Nair. Most people feel mild warmth.', ['Morpheus8 room', 'Nadia and Jordan', 'Skin Night 2025', 'Before and after'][i]));
    add(3, 'go', 'Google profile optimization', 'Google Business Profile', 'Categories, services, attributes, Q and A and photos, all matched to your page.');
    add(1, 'rl', 'Review link and QR code', 'Your front desk', 'lair.to/lumen-review, plus a printable QR card for the front desk.');
    add(31, 'rv', 'Review velocity check', 'Google, Yelp, RealSelf', 'You got 9 reviews this month. Places ranked above you average 14.');
    add(4, 'tf', 'Technical fixes', 'lumenirvine.com', '14 broken links, 3 redirect chains and missing canonical tags.');
    add(11, 'sp', 'Speed optimization', 'lumenirvine.com', 'Mobile load time from 4.8 to under 2 seconds.');
    add(18, 'ur', 'URL restructuring', 'lumenirvine.com', 'One page per treatment, with clean URLs and redirects from the old ones.');
    add(10, 'tm', 'Topical map', 'Your website plan', '120 topics AI connects to lip filler, Botox and Morpheus8, mapped to pages.');
    [17, 24].forEach(d => add(d, 'sc', 'Semantic content: treatment pages', 'lumenirvine.com', 'Rewrites of the lip filler and Morpheus8 pages around the questions people ask AI.'));
    add(22, 'cn', 'Cannibalization fix', 'lumenirvine.com', 'Three pages compete for "lip filler Irvine". We merge them into one.');
    add(25, 'em', 'Entity mapping', 'Everywhere AI reads', 'Ties Lumen, Dr. Nair and each treatment to the same identity across 40 sources.');
    add(22, 'ar', 'Article: Irvine Life, best med spas', 'Irvine Life magazine', 'Pitch and placement in the annual best-of list.', 'Article header');
    [9, 23].forEach(d => add(d, 'bl', 'Blog: what half a syringe really looks like', 'lumenirvine.com', 'Written with Dr. Nair, with before and after photos.'));
    add(29, 'nb', 'Only, first and best story', 'Press, site and page', 'The only med spa in Irvine where the doctor talks you out of more filler. We build that into every source.');
