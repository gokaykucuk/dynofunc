

def get_safe_alias(attr_name):
    return DYNAMO_RESERVED_WORDS.get(attr_name.upper(), attr_name)

DYNAMO_RESERVED_WORDS = {
    'ABORT': '#abort',
    'ABSOLUTE': '#absolute',
    'ACTION': '#action',
    'ADD': '#add',
    'AFTER': '#after',
    'AGENT': '#agent',
    'AGGREGATE': '#aggregate',
    'ALL': '#all',
    'ALLOCATE': '#allocate',
    'ALTER': '#alter',
    'ANALYZE': '#analyze',
    'AND': '#and',
    'ANY': '#any',
    'ARCHIVE': '#archive',
    'ARE': '#are',
    'ARRAY': '#array',
    'AS': '#as',
    'ASC': '#asc',
    'ASCII': '#ascii',
    'ASENSITIVE': '#asensitive',
    'ASSERTION': '#assertion',
    'ASYMMETRIC': '#asymmetric',
    'AT': '#at',
    'ATOMIC': '#atomic',
    'ATTACH': '#attach',
    'ATTRIBUTE': '#attribute',
    'AUTH': '#auth',
    'AUTHORIZATION': '#authorization',
    'AUTHORIZE': '#authorize',
    'AUTO': '#auto',
    'AVG': '#avg',
    'BACK': '#back',
    'BACKUP': '#backup',
    'BASE': '#base',
    'BATCH': '#batch',
    'BEFORE': '#before',
    'BEGIN': '#begin',
    'BETWEEN': '#between',
    'BIGINT': '#bigint',
    'BINARY': '#binary',
    'BIT': '#bit',
    'BLOB': '#blob',
    'BLOCK': '#block',
    'BOOLEAN': '#boolean',
    'BOTH': '#both',
    'BREADTH': '#breadth',
    'BUCKET': '#bucket',
    'BULK': '#bulk',
    'BY': '#by',
    'BYTE': '#byte',
    'CALL': '#call',
    'CALLED': '#called',
    'CALLING': '#calling',
    'CAPACITY': '#capacity',
    'CASCADE': '#cascade',
    'CASCADED': '#cascaded',
    'CASE': '#case',
    'CAST': '#cast',
    'CATALOG': '#catalog',
    'CHAR': '#char',
    'CHARACTER': '#character',
    'CHECK': '#check',
    'CLASS': '#class',
    'CLOB': '#clob',
    'CLOSE': '#close',
    'CLUSTER': '#cluster',
    'CLUSTERED': '#clustered',
    'CLUSTERING': '#clustering',
    'CLUSTERS': '#clusters',
    'COALESCE': '#coalesce',
    'COLLATE': '#collate',
    'COLLATION': '#collation',
    'COLLECTION': '#collection',
    'COLUMN': '#column',
    'COLUMNS': '#columns',
    'COMBINE': '#combine',
    'COMMENT': '#comment',
    'COMMIT': '#commit',
    'COMPACT': '#compact',
    'COMPILE': '#compile',
    'COMPRESS': '#compress',
    'CONDITION': '#condition',
    'CONFLICT': '#conflict',
    'CONNECT': '#connect',
    'CONNECTION': '#connection',
    'CONSISTENCY': '#consistency',
    'CONSISTENT': '#consistent',
    'CONSTRAINT': '#constraint',
    'CONSTRAINTS': '#constraints',
    'CONSTRUCTOR': '#constructor',
    'CONSUMED': '#consumed',
    'CONTINUE': '#continue',
    'CONVERT': '#convert',
    'COPY': '#copy',
    'CORRESPONDING': '#corresponding',
    'COUNT': '#count',
    'COUNTER': '#counter',
    'CREATE': '#create',
    'CROSS': '#cross',
    'CUBE': '#cube',
    'CURRENT': '#current',
    'CURSOR': '#cursor',
    'CYCLE': '#cycle',
    'DATA': '#data',
    'DATABASE': '#database',
    'DATE': '#date',
    'DATETIME': '#datetime',
    'DAY': '#day',
    'DEALLOCATE': '#deallocate',
    'DEC': '#dec',
    'DECIMAL': '#decimal',
    'DECLARE': '#declare',
    'DEFAULT': '#default',
    'DEFERRABLE': '#deferrable',
    'DEFERRED': '#deferred',
    'DEFINE': '#define',
    'DEFINED': '#defined',
    'DEFINITION': '#definition',
    'DELETE': '#delete',
    'DELIMITED': '#delimited',
    'DEPTH': '#depth',
    'DEREF': '#deref',
    'DESC': '#desc',
    'DESCRIBE': '#describe',
    'DESCRIPTOR': '#descriptor',
    'DETACH': '#detach',
    'DETERMINISTIC': '#deterministic',
    'DIAGNOSTICS': '#diagnostics',
    'DIRECTORIES': '#directories',
    'DISABLE': '#disable',
    'DISCONNECT': '#disconnect',
    'DISTINCT': '#distinct',
    'DISTRIBUTE': '#distribute',
    'DO': '#do',
    'DOMAIN': '#domain',
    'DOUBLE': '#double',
    'DROP': '#drop',
    'DUMP': '#dump',
    'DURATION': '#duration',
    'DYNAMIC': '#dynamic',
    'EACH': '#each',
    'ELEMENT': '#element',
    'ELSE': '#else',
    'ELSEIF': '#elseif',
    'EMPTY': '#empty',
    'ENABLE': '#enable',
    'END': '#end',
    'EQUAL': '#equal',
    'EQUALS': '#equals',
    'ERROR': '#error',
    'ESCAPE': '#escape',
    'ESCAPED': '#escaped',
    'EVAL': '#eval',
    'EVALUATE': '#evaluate',
    'EXCEEDED': '#exceeded',
    'EXCEPT': '#except',
    'EXCEPTION': '#exception',
    'EXCEPTIONS': '#exceptions',
    'EXCLUSIVE': '#exclusive',
    'EXEC': '#exec',
    'EXECUTE': '#execute',
    'EXISTS': '#exists',
    'EXIT': '#exit',
    'EXPLAIN': '#explain',
    'EXPLODE': '#explode',
    'EXPORT': '#export',
    'EXPRESSION': '#expression',
    'EXTENDED': '#extended',
    'EXTERNAL': '#external',
    'EXTRACT': '#extract',
    'FAIL': '#fail',
    'FALSE': '#false',
    'FAMILY': '#family',
    'FETCH': '#fetch',
    'FIELDS': '#fields',
    'FILE': '#file',
    'FILTER': '#filter',
    'FILTERING': '#filtering',
    'FINAL': '#final',
    'FINISH': '#finish',
    'FIRST': '#first',
    'FIXED': '#fixed',
    'FLATTERN': '#flattern',
    'FLOAT': '#float',
    'FOR': '#for',
    'FORCE': '#force',
    'FOREIGN': '#foreign',
    'FORMAT': '#format',
    'FORWARD': '#forward',
    'FOUND': '#found',
    'FREE': '#free',
    'FROM': '#from',
    'FULL': '#full',
    'FUNCTION': '#function',
    'FUNCTIONS': '#functions',
    'GENERAL': '#general',
    'GENERATE': '#generate',
    'GET': '#get',
    'GLOB': '#glob',
    'GLOBAL': '#global',
    'GO': '#go',
    'GOTO': '#goto',
    'GRANT': '#grant',
    'GREATER': '#greater',
    'GROUP': '#group',
    'GROUPING': '#grouping',
    'HANDLER': '#handler',
    'HASH': '#hash',
    'HAVE': '#have',
    'HAVING': '#having',
    'HEAP': '#heap',
    'HIDDEN': '#hidden',
    'HOLD': '#hold',
    'HOUR': '#hour',
    'IDENTIFIED': '#identified',
    'IDENTITY': '#identity',
    'IF': '#if',
    'IGNORE': '#ignore',
    'IMMEDIATE': '#immediate',
    'IMPORT': '#import',
    'IN': '#in',
    'INCLUDING': '#including',
    'INCLUSIVE': '#inclusive',
    'INCREMENT': '#increment',
    'INCREMENTAL': '#incremental',
    'INDEX': '#index',
    'INDEXED': '#indexed',
    'INDEXES': '#indexes',
    'INDICATOR': '#indicator',
    'INFINITE': '#infinite',
    'INITIALLY': '#initially',
    'INLINE': '#inline',
    'INNER': '#inner',
    'INNTER': '#innter',
    'INOUT': '#inout',
    'INPUT': '#input',
    'INSENSITIVE': '#insensitive',
    'INSERT': '#insert',
    'INSTEAD': '#instead',
    'INT': '#int',
    'INTEGER': '#integer',
    'INTERSECT': '#intersect',
    'INTERVAL': '#interval',
    'INTO': '#into',
    'INVALIDATE': '#invalidate',
    'IS': '#is',
    'ISOLATION': '#isolation',
    'ITEM': '#item',
    'ITEMS': '#items',
    'ITERATE': '#iterate',
    'JOIN': '#join',
    'KEY': '#key',
    'KEYS': '#keys',
    'LAG': '#lag',
    'LANGUAGE': '#language',
    'LARGE': '#large',
    'LAST': '#last',
    'LATERAL': '#lateral',
    'LEAD': '#lead',
    'LEADING': '#leading',
    'LEAVE': '#leave',
    'LEFT': '#left',
    'LENGTH': '#length',
    'LESS': '#less',
    'LEVEL': '#level',
    'LIKE': '#like',
    'LIMIT': '#limit',
    'LIMITED': '#limited',
    'LINES': '#lines',
    'LIST': '#list',
    'LOAD': '#load',
    'LOCAL': '#local',
    'LOCALTIME': '#localtime',
    'LOCALTIMESTAMP': '#localtimestamp',
    'LOCATION': '#location',
    'LOCATOR': '#locator',
    'LOCK': '#lock',
    'LOCKS': '#locks',
    'LOG': '#log',
    'LOGED': '#loged',
    'LONG': '#long',
    'LOOP': '#loop',
    'LOWER': '#lower',
    'MAP': '#map',
    'MATCH': '#match',
    'MATERIALIZED': '#materialized',
    'MAX': '#max',
    'MAXLEN': '#maxlen',
    'MEMBER': '#member',
    'MERGE': '#merge',
    'METHOD': '#method',
    'METRICS': '#metrics',
    'MIN': '#min',
    'MINUS': '#minus',
    'MINUTE': '#minute',
    'MISSING': '#missing',
    'MOD': '#mod',
    'MODE': '#mode',
    'MODIFIES': '#modifies',
    'MODIFY': '#modify',
    'MODULE': '#module',
    'MONTH': '#month',
    'MULTI': '#multi',
    'MULTISET': '#multiset',
    'NAME': '#name',
    'NAMES': '#names',
    'NATIONAL': '#national',
    'NATURAL': '#natural',
    'NCHAR': '#nchar',
    'NCLOB': '#nclob',
    'NEW': '#new',
    'NEXT': '#next',
    'NO': '#no',
    'NONE': '#none',
    'NOT': '#not',
    'NULL': '#null',
    'NULLIF': '#nullif',
    'NUMBER': '#number',
    'NUMERIC': '#numeric',
    'OBJECT': '#object',
    'OF': '#of',
    'OFFLINE': '#offline',
    'OFFSET': '#offset',
    'OLD': '#old',
    'ON': '#on',
    'ONLINE': '#online',
    'ONLY': '#only',
    'OPAQUE': '#opaque',
    'OPEN': '#open',
    'OPERATOR': '#operator',
    'OPTION': '#option',
    'OR': '#or',
    'ORDER': '#order',
    'ORDINALITY': '#ordinality',
    'OTHER': '#other',
    'OTHERS': '#others',
    'OUT': '#out',
    'OUTER': '#outer',
    'OUTPUT': '#output',
    'OVER': '#over',
    'OVERLAPS': '#overlaps',
    'OVERRIDE': '#override',
    'OWNER': '#owner',
    'PAD': '#pad',
    'PARALLEL': '#parallel',
    'PARAMETER': '#parameter',
    'PARAMETERS': '#parameters',
    'PARTIAL': '#partial',
    'PARTITION': '#partition',
    'PARTITIONED': '#partitioned',
    'PARTITIONS': '#partitions',
    'PATH': '#path',
    'PERCENT': '#percent',
    'PERCENTILE': '#percentile',
    'PERMISSION': '#permission',
    'PERMISSIONS': '#permissions',
    'PIPE': '#pipe',
    'PIPELINED': '#pipelined',
    'PLAN': '#plan',
    'POOL': '#pool',
    'POSITION': '#position',
    'PRECISION': '#precision',
    'PREPARE': '#prepare',
    'PRESERVE': '#preserve',
    'PRIMARY': '#primary',
    'PRIOR': '#prior',
    'PRIVATE': '#private',
    'PRIVILEGES': '#privileges',
    'PROCEDURE': '#procedure',
    'PROCESSED': '#processed',
    'PROJECT': '#project',
    'PROJECTION': '#projection',
    'PROPERTY': '#property',
    'PROVISIONING': '#provisioning',
    'PUBLIC': '#public',
    'PUT': '#put',
    'QUERY': '#query',
    'QUIT': '#quit',
    'QUORUM': '#quorum',
    'RAISE': '#raise',
    'RANDOM': '#random',
    'RANGE': '#range',
    'RANK': '#rank',
    'RAW': '#raw',
    'READ': '#read',
    'READS': '#reads',
    'REAL': '#real',
    'REBUILD': '#rebuild',
    'RECORD': '#record',
    'RECURSIVE': '#recursive',
    'REDUCE': '#reduce',
    'REF': '#ref',
    'REFERENCE': '#reference',
    'REFERENCES': '#references',
    'REFERENCING': '#referencing',
    'REGEXP': '#regexp',
    'REGION': '#region',
    'REINDEX': '#reindex',
    'RELATIVE': '#relative',
    'RELEASE': '#release',
    'REMAINDER': '#remainder',
    'RENAME': '#rename',
    'REPEAT': '#repeat',
    'REPLACE': '#replace',
    'REQUEST': '#request',
    'RESET': '#reset',
    'RESIGNAL': '#resignal',
    'RESOURCE': '#resource',
    'RESPONSE': '#response',
    'RESTORE': '#restore',
    'RESTRICT': '#restrict',
    'RESULT': '#result',
    'RETURN': '#return',
    'RETURNING': '#returning',
    'RETURNS': '#returns',
    'REVERSE': '#reverse',
    'REVOKE': '#revoke',
    'RIGHT': '#right',
    'ROLE': '#role',
    'ROLES': '#roles',
    'ROLLBACK': '#rollback',
    'ROLLUP': '#rollup',
    'ROUTINE': '#routine',
    'ROW': '#row',
    'ROWS': '#rows',
    'RULE': '#rule',
    'RULES': '#rules',
    'SAMPLE': '#sample',
    'SATISFIES': '#satisfies',
    'SAVE': '#save',
    'SAVEPOINT': '#savepoint',
    'SCAN': '#scan',
    'SCHEMA': '#schema',
    'SCOPE': '#scope',
    'SCROLL': '#scroll',
    'SEARCH': '#search',
    'SECOND': '#second',
    'SECTION': '#section',
    'SEGMENT': '#segment',
    'SEGMENTS': '#segments',
    'SELECT': '#select',
    'SELF': '#self',
    'SEMI': '#semi',
    'SENSITIVE': '#sensitive',
    'SEPARATE': '#separate',
    'SEQUENCE': '#sequence',
    'SERIALIZABLE': '#serializable',
    'SESSION': '#session',
    'SET': '#set',
    'SETS': '#sets',
    'SHARD': '#shard',
    'SHARE': '#share',
    'SHARED': '#shared',
    'SHORT': '#short',
    'SHOW': '#show',
    'SIGNAL': '#signal',
    'SIMILAR': '#similar',
    'SIZE': '#size',
    'SKEWED': '#skewed',
    'SMALLINT': '#smallint',
    'SNAPSHOT': '#snapshot',
    'SOME': '#some',
    'SOURCE': '#source',
    'SPACE': '#space',
    'SPACES': '#spaces',
    'SPARSE': '#sparse',
    'SPECIFIC': '#specific',
    'SPECIFICTYPE': '#specifictype',
    'SPLIT': '#split',
    'SQL': '#sql',
    'SQLCODE': '#sqlcode',
    'SQLERROR': '#sqlerror',
    'SQLEXCEPTION': '#sqlexception',
    'SQLSTATE': '#sqlstate',
    'SQLWARNING': '#sqlwarning',
    'START': '#start',
    'STATE': '#state',
    'STATIC': '#static',
    'STATUS': '#status',
    'STORAGE': '#storage',
    'STORE': '#store',
    'STORED': '#stored',
    'STREAM': '#stream',
    'STRING': '#string',
    'STRUCT': '#struct',
    'STYLE': '#style',
    'SUB': '#sub',
    'SUBMULTISET': '#submultiset',
    'SUBPARTITION': '#subpartition',
    'SUBSTRING': '#substring',
    'SUBTYPE': '#subtype',
    'SUM': '#sum',
    'SUPER': '#super',
    'SYMMETRIC': '#symmetric',
    'SYNONYM': '#synonym',
    'SYSTEM': '#system',
    'TABLE': '#table',
    'TABLESAMPLE': '#tablesample',
    'TEMP': '#temp',
    'TEMPORARY': '#temporary',
    'TERMINATED': '#terminated',
    'TEXT': '#text',
    'THAN': '#than',
    'THEN': '#then',
    'THROUGHPUT': '#throughput',
    'TIME': '#time',
    'TIMESTAMP': '#timestamp',
    'TIMEZONE': '#timezone',
    'TINYINT': '#tinyint',
    'TO': '#to',
    'TOKEN': '#token',
    'TOTAL': '#total',
    'TOUCH': '#touch',
    'TRAILING': '#trailing',
    'TRANSACTION': '#transaction',
    'TRANSFORM': '#transform',
    'TRANSLATE': '#translate',
    'TRANSLATION': '#translation',
    'TREAT': '#treat',
    'TRIGGER': '#trigger',
    'TRIM': '#trim',
    'TRUE': '#true',
    'TRUNCATE': '#truncate',
    'TTL': '#ttl',
    'TUPLE': '#tuple',
    'TYPE': '#type',
    'UNDER': '#under',
    'UNDO': '#undo',
    'UNION': '#union',
    'UNIQUE': '#unique',
    'UNIT': '#unit',
    'UNKNOWN': '#unknown',
    'UNLOGGED': '#unlogged',
    'UNNEST': '#unnest',
    'UNPROCESSED': '#unprocessed',
    'UNSIGNED': '#unsigned',
    'UNTIL': '#until',
    'UPDATE': '#update',
    'UPPER': '#upper',
    'URL': '#url',
    'USAGE': '#usage',
    'USE': '#use',
    'USER': '#user',
    'USERS': '#users',
    'USING': '#using',
    'UUID': '#uuid',
    'VACUUM': '#vacuum',
    'VALUE': '#value',
    'VALUED': '#valued',
    'VALUES': '#values',
    'VARCHAR': '#varchar',
    'VARIABLE': '#variable',
    'VARIANCE': '#variance',
    'VARINT': '#varint',
    'VARYING': '#varying',
    'VIEW': '#view',
    'VIEWS': '#views',
    'VIRTUAL': '#virtual',
    'VOID': '#void',
    'WAIT': '#wait',
    'WHEN': '#when',
    'WHENEVER': '#whenever',
    'WHERE': '#where',
    'WHILE': '#while',
    'WINDOW': '#window',
    'WITH': '#with',
    'WITHIN': '#within',
    'WITHOUT': '#without',
    'WORK': '#work',
    'WRAPPED': '#wrapped',
    'WRITE': '#write',
    'YEAR': '#year',
    'ZONE': '#zone'
}
