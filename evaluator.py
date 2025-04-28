from models import Policy, Request

class PolicyEvaluator:
    def __init__(self, policies):
        self.policies = policies

    def evaluate_request(self, request: Request) -> (str, str):
        allow_policies = []
        deny_policies = []

        for policy in self.policies:
            if self._matches(policy, request):
                if policy.condition:
                    if not self._evaluate_condition(policy.condition, request):
                        continue
                if policy.effect.lower() == "deny":
                    deny_policies.append(policy)
                elif policy.effect.lower() == "allow":
                    allow_policies.append(policy)

        if deny_policies:
            explanation = f"DENY due to matching deny policy: {self._policy_summary(deny_policies[0])}"
            return "DENY", explanation
        elif allow_policies:
            explanation = f"ALLOW due to matching allow policy: {self._policy_summary(allow_policies[0])}"
            return "ALLOW", explanation
        else:
            explanation = "DENY because no matching allow policy found."
            return "DENY", explanation

    def _matches(self, policy: Policy, request: Request) -> bool:
        return (self._match_field(policy.principal, request.principal["id"]) and
                policy.action == request.action and
                self._match_field(policy.resource, request.resource["id"]))

    def _match_field(self, policy_value: str, request_value: str) -> bool:
        if policy_value == "*" or policy_value.endswith("::*"):
            prefix = policy_value[:-2]  # remove '::*'
            return request_value.startswith(prefix)
        else:
            return policy_value == request_value

    def _evaluate_condition(self, condition: str, request: Request) -> bool:
        try:
            parts = [part.strip() for part in condition.split('&&')]
            for part in parts:
                if "==" in part:
                    lhs, rhs = part.split("==")
                    lhs_val = self._resolve_field(lhs.strip(), request)
                    rhs_val = self._resolve_field(rhs.strip(), request)
                    if str(lhs_val) != str(rhs_val):
                        return False
                else:
                    return False
            return True
        except Exception as e:
            print(f"Condition evaluation error: {e}")
            return False

    def _resolve_field(self, field: str, request: Request):
        if field == "true":
            return True
        if field == "false":
            return False
        if "." in field:
            object_name, attribute = field.split(".")
            if object_name == "resource":
                return request.resource.get(attribute)
            if object_name == "principal":
                return request.principal.get(attribute)
        return field

    def _policy_summary(self, policy: Policy) -> str:
        return f"(Principal: {policy.principal}, Action: {policy.action}, Resource: {policy.resource}, Effect: {policy.effect})"
