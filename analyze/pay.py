from boto.mturk.connection import MTurkConnection
from boto.mturk.price import Price

#ACCESS_ID = 'AKIAID3UBXF43NAUDSRQ'
#SECRET_KEY = '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'

ACCESS_ID = 'AKIAJUIWAR2Q2YQG2VAQ'
SECRET_KEY = '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'


HOST = 'mechanicalturk.amazonaws.com'

mturk = MTurkConnection(aws_access_key_id=ACCESS_ID,
        aws_secret_access_key=SECRET_KEY,
        host=HOST)
hits = mturk.get_all_hits()

def decode(code):
    mapping = ['D','E','F','B','G','M','N','A','I','L']
    res = ""
    for c in code:
        if c != 'O':
            try:
                res += str(mapping.index(c))
            except:
                return '-1'
        else:
            res += '_'
    return res

def bonus(workerId, assignmentId):
    print 'Bonus', workerId
def approve(workerId, assignmentId):
    print 'approve', workerId
def reject(workerId, assignmentId):
    print 'reject', workerId

for hit in hits:
    print "hit ID: ", hit.HITId
    assignments = mturk.get_assignments(hit.HITId, page_size=100)
    print len(assignments)
    for assignment in assignments:
        print assignment.WorkerId
        answers = assignment.answers[0]
        code = "-1"
        for answer in answers:
            if answer.qid == 'Q5FreeTextInput':
                code = decode(answer.fields[0])

        if code != '-1':
            if(code.find('_') != -1):
                bonus(assignment.WorkerId, assignment.AssignmentId)
            else:
                approve(assignment.WorkerId, assignment.AssignmentId)
        else:
            reject(assignment.WorkerId, assignment.AssignmentId)

