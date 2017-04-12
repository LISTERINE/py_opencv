from flask import render_template, request, Blueprint
import json

errors= Blueprint("errors", __name__)

@errors.errorhandler(404)
def not_found_error(error):
    agent_fields = [request.user_agent.browser, request.user_agent.version, request.user_agent.platform]
    user_agent = ",".join(s for s in agent_fields if isinstance(s,basestring))
    referrer = request.referrer if request.referrer is not None else ""
    info = {"base_url": request.base_url,
            "full_path": request.full_path,
            "url": request.url,
            "user_agent": user_agent,
            "method": request.method,
            "remote_addr": request.remote_addr,
            "referrer": referrer}
    app.logger.exception(json.dumps(info))
    return render_template('404.html'), 404


@errors.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
